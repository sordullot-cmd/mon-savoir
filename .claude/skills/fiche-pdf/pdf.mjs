#!/usr/bin/env node
/**
 * Rend une fiche condensée (markdown Obsidian) en PDF A4 imprimable.
 *
 *   node .claude/skills/fiche-pdf/pdf.mjs "eco gestion/_condenses/<nom>.md"
 *   → écrit <nom>.pdf à côté du .md, et affiche son chemin.
 *
 * La mise en forme (et ses règles) est décrite dans le SKILL.md voisin.
 *
 * Le markdown passe par le même moteur que le site (vault-gallery/scripts/
 * markdown.mjs) : callouts, formules KaTeX et ancres sont rendus à l'identique.
 * Ce script n'ajoute que ce qui est propre au vault (embeds `![[x.svg]]`,
 * wikilinks, `==surligné==`) et une feuille de style faite pour le papier. Le
 * PDF est imprimé par Chrome en mode headless : aucune dépendance à installer.
 */
import { readFileSync, writeFileSync, existsSync, readdirSync, statSync, mkdtempSync } from 'node:fs'
import { join, dirname, basename, resolve } from 'node:path'
import { pathToFileURL, fileURLToPath } from 'node:url'
import { execFileSync } from 'node:child_process'
import { tmpdir } from 'node:os'

const ICI = dirname(fileURLToPath(import.meta.url))
const VAULT = resolve(ICI, '../../..')
const SITE = process.env.SITE_PATH || join(process.env.HOME, 'Documents/GitHub/vault-gallery')
const CHROME = [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
].find(existsSync)

const source = process.argv[2]
if (!source) {
  console.error('usage : node pdf.mjs <fiche condensée.md> [sortie.pdf]')
  process.exit(1)
}
const entree = resolve(source)
const sortie = resolve(process.argv[3] || entree.replace(/\.md$/, '.pdf'))
if (!existsSync(join(SITE, 'scripts/markdown.mjs'))) {
  console.error(`moteur markdown introuvable : ${SITE}/scripts/markdown.mjs (SITE_PATH ?)`)
  process.exit(1)
}
if (!CHROME) {
  console.error('Chrome introuvable : il imprime le PDF.')
  process.exit(1)
}

const { configureMarked } = await import(pathToFileURL(join(SITE, 'scripts/markdown.mjs')).href)
const marked = configureMarked()

/* ------------------------------------------------------------ le markdown */

let md = readFileSync(entree, 'utf8')
const fm = {}
md = md.replace(/^---\n([\s\S]*?)\n---\n/, (_, bloc) => {
  for (const l of bloc.split('\n')) {
    const m = /^(\w+):\s*(.+)$/.exec(l)
    if (m) fm[m[1]] = m[2].replace(/^["']|["']$/g, '')
  }
  return ''
})

/** Fichiers du vault par nom, pour résoudre `![[x.svg]]` comme Obsidian. */
const fichiers = new Map()
const IGNORES = new Set(['.git', '.obsidian', 'node_modules', '.claude', 'INSPIRATION'])
;(function parcours(dir) {
  for (const nom of readdirSync(dir)) {
    if (IGNORES.has(nom)) continue
    const p = join(dir, nom)
    const s = statSync(p)
    if (s.isDirectory()) parcours(p)
    else if (!fichiers.has(nom)) fichiers.set(nom.normalize('NFC'), p)
  }
})(VAULT)

const IMAGE = /\.(svg|png|jpe?g|webp|gif)$/i
md = md
  // Embeds : l'image elle-même, à sa largeur demandée (`|300`) le cas échéant.
  .replace(/!\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]/g, (tout, nom, opt) => {
    const p = fichiers.get(nom.trim().normalize('NFC'))
    if (!p || !IMAGE.test(p)) return ''
    const largeur = /^\d+$/.test(opt || '') ? ` style="width:${opt}px"` : ''
    return `<img class="schema" src="${pathToFileURL(p).href}" alt=""${largeur}>`
  })
  // Wikilinks : leur texte, le papier ne suit pas les liens.
  .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '$2')
  .replace(/\[\[(?:[^\]#]*#)?([^\]]+)\]\]/g, '$1')
  // Un `=` seul peut vivre dans le surligné (`==prix = coût + marge==`).
  .replace(/==((?:[^=\n]|=(?!=))+?)==/g, '<mark>$1</mark>')
  // `~5 %` veut dire « environ » : en GFM, deux tildes simples barreraient le
  // texte entre eux. Seul `~~barré~~` garde son sens.
  .replace(/(^|[^~\\])~(?!~)/gm, '$1\\~')

const corps = marked.parse(md)

/* ------------------------------------------------------------- la page */

const titre = fm.titre || (/^# (.+)$/m.exec(md)?.[1] ?? basename(entree, '.md'))
const katexCss = pathToFileURL(join(SITE, 'node_modules/katex/dist/katex.min.css')).href
// La date est celle du condensé (frontmatter `condense:`), pas celle du rendu :
// relancer le script pour un réglage de style ne rajeunit pas le contenu.
const jour = /^\d{4}-\d{2}-\d{2}$/.test(fm.condense || '') ? new Date(fm.condense + 'T12:00') : new Date()
const date = jour.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' })
const pied = [fm.matiere, `condensé le ${date}`].filter(Boolean).join(' · ')
// `etat: en cours` : le chapitre n'est pas fini au cours, le PDF le dit en tête.
const enCours = /^en cours$/i.test(fm.etat || '')
const bandeau = enCours
  ? `<p class="en-cours">Chapitre en cours — ce condensé s'arrête où en est le cours${fm.jusqua ? ` (${fm.jusqua.replace(/</g, '&lt;')})` : ''}, il sera complété.</p>`
  : ''
const entete = (fm.matiere || '').replace(/["\\]/g, '')

const html = `<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<title>${titre.replace(/</g, '&lt;')}</title>
<link rel="stylesheet" href="${katexCss}">
<style>
  @page {
    size: A4; margin: 11mm 12mm 13mm;
    @bottom-left { content: "${entete}"; font: 7.4pt -apple-system, Helvetica, sans-serif; color: #8a909c; }
    @bottom-right { content: counter(page) " / " counter(pages); font: 7.4pt -apple-system, Helvetica, sans-serif; color: #8a909c; }
  }
  :root {
    --encre: #16181d; --gris: #5d6370; --filet: #d9dce2; --fond: #f4f5f7;
    --alerte: #d92d5e; --prudence: #c2761a; --test: #10b981; --astuce: #0e8ba8; --resume: #1f2a44;
  }
  * { box-sizing: border-box; }
  html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body {
    margin: 0; color: var(--encre); background: #fff;
    font: 9.4pt/1.42 -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif;
    hyphens: auto; text-wrap: pretty;
  }
  h1 { font-size: 17pt; line-height: 1.15; letter-spacing: -0.3px; margin: 0 0 1.5mm; }
  h1 + p { color: var(--gris); margin-top: 0; }
  h2 {
    font-size: 11pt; margin: 4.2mm 0 1.6mm; padding-bottom: 0.8mm;
    border-bottom: 1.4px solid var(--encre); break-after: avoid;
  }
  h3 { font-size: 9.8pt; margin: 2.8mm 0 1mm; break-after: avoid; }
  h4 { font-size: 9.4pt; margin: 2mm 0 0.6mm; color: var(--gris); break-after: avoid; }
  p { margin: 1mm 0; }
  ul, ol { margin: 1mm 0; padding-left: 4.6mm; }
  li { margin: 0.35mm 0; }
  li > ul, li > ol { margin: 0.3mm 0; }
  strong { font-weight: 650; }
  mark { background: #fff1a8; padding: 0 0.5mm; }
  code { font: 8.6pt/1.3 ui-monospace, Menlo, monospace; background: var(--fond); padding: 0 0.8mm; border-radius: 2px; }
  hr { border: 0; border-top: 1px solid var(--filet); margin: 3mm 0; }
  blockquote { margin: 1.4mm 0; padding: 0.6mm 3mm; border-left: 2.5px solid var(--encre); background: var(--fond); }
  table { width: 100%; border-collapse: collapse; margin: 1.6mm 0; font-size: 8.8pt; break-inside: avoid; }
  th, td { border: 1px solid var(--filet); padding: 0.9mm 1.6mm; text-align: left; vertical-align: top; }
  th { background: var(--fond); font-weight: 650; }
  td:first-child, th:first-child { hyphens: manual; }
  /* Les lignes vides des tableaux « à ne pas confondre » séparent les paires. */
  tr:has(td:empty:first-child + td:empty:last-child) td { padding: 0; height: 1.1mm; border-left: 0; border-right: 0; }
  img.schema { display: block; max-width: 60%; max-height: 48mm; margin: 1.6mm auto; break-inside: avoid; }
  /* Plusieurs schémas sur une même ligne du markdown : côte à côte. */
  p:has(> img.schema + img.schema) { display: flex; justify-content: center; align-items: center; gap: 8mm; margin: 1.6mm 0; }
  p > img.schema + img.schema, p:has(> img.schema + img.schema) > img.schema { margin: 0; max-width: 46%; }
  em:only-child { color: var(--gris); }
  .math-bloc { margin: 1.4mm 0; text-align: center; }
  .katex { font-size: 1.05em; }

  .callout {
    margin: 2mm 0; padding: 1.6mm 2.6mm; border: 1px solid var(--filet);
    border-left: 2.5px solid var(--gris); border-radius: 2mm; background: var(--fond);
    break-inside: avoid;
  }
  .callout-title { margin: 0 0 0.6mm; font-weight: 700; font-size: 9.4pt; list-style: none; }
  .callout-body > :first-child { margin-top: 0; }
  .callout-body > :last-child { margin-bottom: 0; }
  .callout-alerte { border-left-color: var(--alerte); } .callout-alerte .callout-title { color: var(--alerte); }
  .callout-prudence { border-left-color: var(--prudence); } .callout-prudence .callout-title { color: var(--prudence); }
  .callout-test { border-left-color: var(--test); }
  .callout-astuce { border-left-color: var(--astuce); } .callout-astuce .callout-title { color: var(--astuce); }
  .callout-resume { border-left-color: var(--resume); background: #eef1f7; }
  details summary::-webkit-details-marker { display: none; }

  .en-cours {
    margin: 0 0 2mm; padding: 1mm 2.6mm; border-radius: 2mm; font-size: 8.4pt;
    background: #fdf3e4; color: #8a4f0c; border: 1px solid #f1d3a6;
  }
  footer { margin-top: 4mm; padding-top: 1.4mm; border-top: 1px solid var(--filet); color: var(--gris); font-size: 7.6pt; }
</style></head>
<body>
${corps.replace(/(<\/h1>\s*(?:<p>[\s\S]*?<\/p>)?)/, `$1${bandeau}`)}
<footer>${pied}</footer>
</body></html>`

/* ----------------------------------------------------------- l'impression */

// Le HTML vit à côté du scratch, pas du .md : seul le PDF reste dans le vault.
// `file://` partout, pour que Chrome lise schémas et polices KaTeX en local.
const tmp = mkdtempSync(join(tmpdir(), 'condense-'))
const page = join(tmp, 'page.html')
// Repliables (Contrôle) : ouverts sur papier, il n'y a pas de clic.
writeFileSync(page, html.replace(/<details class=/g, '<details open class='))

execFileSync(
  CHROME,
  [
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--allow-file-access-from-files',
    '--virtual-time-budget=4000',
    `--print-to-pdf=${sortie}`,
    pathToFileURL(page).href,
  ],
  { stdio: ['ignore', 'ignore', 'pipe'] }
)

if (!existsSync(sortie)) {
  console.error('Chrome n’a pas produit de PDF.')
  process.exit(1)
}
// Le nombre de pages dit si le condensé tient sa promesse (2 pages max).
const pages = (readFileSync(sortie, 'latin1').match(/\/Type\s*\/Page[^s]/g) || []).length
console.log(`${sortie}\n${pages} page${pages > 1 ? 's' : ''}`)
