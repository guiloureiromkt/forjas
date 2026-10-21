# {{ aluno.nome }} — Propagação (Brand System → ecossistema)

> Output da Estação 12 de A Forja da Alma · sessão {{ session.data }}.

Os 7 arquivos são a camada canônica "quem é {{ aluno.nome_curto | default(aluno.nome) }}" — lida por todas as skills.

## Matriz · arquivo → quem consome
| Arquivo | Consumidor |
|---|---|
| `{{ aluno.nome_curto_slug }}-brand.md` | todas (identidade · tese) |
| `{{ aluno.nome_curto_slug }}-voice.md` | skills de conteúdo (post · carrossel · newsletter · vídeo) |
| `{{ aluno.nome_curto_slug }}-design-system.md` | skills visuais (redesign · imagem · landing) |
| `{{ aluno.nome_curto_slug }}-inimigos.md` | skills de copy externa |
| `{{ aluno.nome_curto_slug }}-publico.md` | todas (segmentação) |
| `{{ aluno.nome_curto_slug }}-feedback-loops.md` | trackers (drift de voz) |

## Status
- ✅ Os 7 arquivos gerados.
- ⚠️ Conflito com material antigo → **estes 7 ganham** (destilação curada).

---
**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
