# Contrato do Brand System (output da Forja da Alma v2.0)

> A Forja da Alma compila os 7 arquivos abaixo, na pasta `marca/`. É o formato que as outras Forjas e as ferramentas de produção leem.

| # | Arquivo | O que contém | Quem consome (downstream) | Vem de |
|---|---|---|---|---|
| 1 | `<marca>-brand.md` | identidade · tese central · missão · princípios não-negociáveis · decisões pré-programadas · repertório · arquétipo · StoryBrand (herói/guia) | todas as skills | Estações 1-4, 8, 9 |
| 2 | `<marca>-voice.md` | tom dominante · marcadores linguísticos · vocabulário hub · zona proibida · construções | blog · linkedin · carrossel · newsletter | Estação 5 |
| 3 | `<marca>-design-system.md` | paleta (core+categóricas) · tipografia · logo/marca · tokens · componentes · world building | page-redesign · image-pipeline · landing · carrossel | Estação 5B 🆕 |
| 4 | `<marca>-inimigos.md` | 3 inimigos nomeados · renegado (público) · posicionamento competitivo | linkedin · blog (copy externa) | Estação 6 🆕 standalone |
| 5 | `<marca>-publico.md` | ICP · demografia · dores · medos · tensões · jornada · códigos | todas (segmentação) | Master Brief §5.3 🆕 |
| 6 | `<marca>-feedback-loops.md` | sistema vivo · gatilhos · o que alimentar pós-publicação | trackers | Estação evolutiva |
| 7 | `<marca>-propagation.md` | matriz descoberta × destino · plano P0-P3 (genérico) | meta | Estação 12 |

## Regras do contrato
- **Cada arquivo é standalone** (a skill que precisa de voz lê só `voice.md`; quem precisa de visual lê só `design-system.md`).
- **Frontmatter YAML** em cada um: `type · marca · date · confianca`.
- **Níveis de confiança** em achados estruturais (🟢🟡🔴).
- **Compatível multi-LLM:** "Nasce em Claude · roda em qualquer LLM."
- **Master Brief §5.4** lista e linka os 7.

## O que mudou da v1 (3 → 7)
- **+** `design-system.md` (a camada visual que faltava)
- **+** `inimigos.md` standalone (era seção dentro de brand)
- **+** `publico.md` (vem do Master Brief / pesquisa-forja · engine PÚBLICO)
- Os 4 pilares de Personal Branding distribuídos (arquétipos+StoryBrand → brand · world building → design · conteúdo 2026/GEO → Campo de Batalha)
