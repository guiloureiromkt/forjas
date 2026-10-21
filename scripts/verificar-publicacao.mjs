#!/usr/bin/env node
// ============================================================================
// verificar-publicacao.mjs — o portão antes de qualquer versão das Forjas sair.
//
// Procura duas coisas que passam na revisão de quem escreveu:
//   1. o que só existe na máquina de quem escreveu (caminho de pasta pessoal,
//      vault, cofre, credencial, código de caderno) e nome de pessoa ou cliente;
//   2. caminho do pacote que não existe: `${CLAUDE_PLUGIN_ROOT}/...` ou
//      `<pasta do pacote>/...` apontando para um arquivo que não está aqui.
//      A validação do Claude Code não pega isso; só a instalação, tarde demais.
//
// Nomes de pessoas e clientes NÃO ficam escritos neste arquivo: ele é público,
// e uma lista de nomes privados dentro do verificador é ela mesma o vazamento.
// Passe a lista num arquivo de texto, um termo por linha, fora do pacote:
//
//   FORJAS_NOMES_PRIVADOS=/caminho/nomes.txt node scripts/verificar-publicacao.mjs
//
// Sai com código 1 se achar bloqueio. "Confere" só avisa.
// ============================================================================

import fs from "node:fs";
import path from "node:path";

const EU = path.resolve(new URL(import.meta.url).pathname);
const RAIZ = path.resolve(process.argv[2] || path.join(path.dirname(EU), ".."));

const REGRAS = [
  { id: "pasta-pessoal", sev: "bloqueia", re: /\/home\/(?!SEU-USUARIO)[A-Za-z0-9_.-]+|\/Users\/(?!SEU-USUARIO)[A-Za-z0-9_.-]+|C:\\Users\\(?!SEU-USUARIO)[A-Za-z0-9_.-]+/g,
    diz: "caminho da máquina de quem escreveu" },
  { id: "skills-pessoais", sev: "bloqueia", re: /~\/\.claude\/skills/g,
    diz: "aponta para skills instaladas à mão em outra máquina; dentro do pacote, use ${CLAUDE_PLUGIN_ROOT}" },
  { id: "vault", sev: "bloqueia", re: /\b(10_Canon|90_Meta|20_Projetos|01_Raw|00_Inbox|_PENDING-SYNC|GuiOS)\b/g,
    diz: "referência a um vault pessoal; a skill não funciona sem ele" },
  { id: "cofre", sev: "bloqueia", re: /\.secrets|secrets\.env|id_rsa|\.pem\b|\.credentials\.json/g,
    diz: "caminho de cofre de credenciais" },
  { id: "credencial", sev: "bloqueia", re: /\b(sk-[A-Za-z0-9]{16,}|r8_[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,}|AIza[A-Za-z0-9_-]{20,})\b/g,
    diz: "isso tem cara de credencial de verdade" },
  { id: "uuid", sev: "bloqueia", re: /\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/gi,
    diz: "identificador de algo privado (caderno, documento, conta)" },
  { id: "dinheiro", sev: "confere", re: /R\$\s?\d[\d.,]*/g,
    diz: "valor em reais: exemplo do método está bem; preço de quem escreveu, não" },
  { id: "email", sev: "confere", re: /\b[a-z0-9._%+-]+@(?!exemplo|example|seu|suamarca|meusite)[a-z0-9.-]+\.[a-z]{2,}\b/gi,
    diz: "e-mail real no texto" },
];

const ARQ_NOMES = process.env.FORJAS_NOMES_PRIVADOS;
if (ARQ_NOMES) {
  const termos = fs.readFileSync(ARQ_NOMES, "utf8").split("\n").map((s) => s.trim()).filter((s) => s && !s.startsWith("#"));
  if (termos.length) {
    const esc = termos.map((s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    REGRAS.push({ id: "nome-privado", sev: "bloqueia", re: new RegExp(`(?<![\\p{L}\\d])(${esc.join("|")})(?![\\p{L}\\d])`, "giu"),
      diz: "nome de pessoa, cliente ou projeto privado (lista fora do pacote)" });
  }
} else {
  console.log("aviso: FORJAS_NOMES_PRIVADOS não definido — nomes privados não foram procurados");
}

function arquivos(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === ".git" || e.name === "node_modules") continue;
    const p = path.join(dir, e.name);
    e.isDirectory() ? arquivos(p, acc) : acc.push(p);
  }
  return acc;
}

const lista = arquivos(RAIZ).filter((f) => /\.(md|json|mjs|js|py|txt|ya?ml|sh|j2)$/i.test(f) || path.basename(f) === "LICENSE");
const achados = [];
const CAMINHO = /(?:\$\{CLAUDE_PLUGIN_ROOT\}|<pasta do pacote>)\/([^\s`'")\]]+)/g;

for (const f of lista) {
  const texto = fs.readFileSync(f, "utf8");
  const rel = path.relative(RAIZ, f);
  const souEu = path.resolve(f) === EU;
  texto.split("\n").forEach((linha, i) => {
    if (!souEu) {
      for (const regra of REGRAS) {
        regra.re.lastIndex = 0;
        const m = linha.match(regra.re);
        if (m) achados.push({ arquivo: rel, linha: i + 1, regra, trecho: [...new Set(m)].join(" · "), contexto: linha.trim().slice(0, 110) });
      }
    }
    for (const m of linha.matchAll(CAMINHO)) {
      const alvo = m[1].replace(/[.,;:]+$/, "");
      if (/[<>*{]/.test(alvo)) continue; // modelo de caminho, não caminho
      if (!fs.existsSync(path.join(RAIZ, alvo))) {
        achados.push({ arquivo: rel, linha: i + 1,
          regra: { sev: "bloqueia", diz: "caminho do pacote que não existe aqui" }, trecho: alvo, contexto: linha.trim().slice(0, 110) });
      }
    }
  });
}

const bloqueios = achados.filter((a) => a.regra.sev === "bloqueia");
const conferir = achados.filter((a) => a.regra.sev === "confere");
console.log(`\nVERIFICAÇÃO DE PUBLICAÇÃO · ${lista.length} arquivo(s) em ${RAIZ}`);
const mostra = (titulo, itens) => {
  if (!itens.length) return;
  console.log(`\n${titulo} (${itens.length})`);
  for (const a of itens) console.log(`  ${a.arquivo}:${a.linha} · ${a.regra.diz}\n    → ${a.trecho}\n    | ${a.contexto}`);
};
mostra("🔴 BLOQUEIA", bloqueios);
mostra("🟡 CONFERE", conferir);
console.log(achados.length ? `\n${bloqueios.length} bloqueio(s) · ${conferir.length} para conferir\n` : "\nnenhum bloqueio · nada para conferir\n");
process.exit(bloqueios.length ? 1 : 0);
