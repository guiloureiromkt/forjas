# Modo 5.5 · Risk Audit + Modo 6.5 · Pre-Launch Asset Manifest (detalhe canon)

> **Quando ler:** (a) Modo 5.5 — sempre, antes de finalizar o Dispatcher da Etapa 5; (b) Modo 6.5 — SÓ quando o aluno declara marco data-fixa. Conteúdo movido verbatim do SKILL.md em 2026-07-13 (reestruturação progressive disclosure). Ambos canon absorvido de `marketing:campaign-plan` (Anthropic) 2026-05-25 noite.

---

## Modo 5.5 · Risk Audit por campanha (Ganho #7 absorvido)

Antes de finalizar Etapa 5 Dispatcher, executar Risk Audit do plano:
- Identificar **2-3 riscos** específicos da campanha do aluno
- **Mitigation strategy** explícita para cada
- **Probabilidade × Impacto** matriz (baixa/média/alta cada)

**Categorias canon de risco a investigar:**

1. **Risco de timeline** — data fixa que não cabe na produção (cruza com o prazo real de produção de cada formato: um pillar leva de 5 a 10 dias, um vídeo de lançamento de 2 a 4 semanas)
2. **Risco de audiência mismatch** — peça pra ICP errado (Principal vs Secundário · misturados sem propósito)
3. **Risco de canal underperformance** — depender de 1 canal único · violação Hub-Spoke 1-3-5 (DC51)
4. **Risco regulatório/político** — LGPD (DC58 WhatsApp double opt-in) · cicatriz vs ferida aberta (DC46)
5. **Risco de algoritmo** — link no corpo/1º comentário (DC54) · cadência insustentável >4h/sem · sameness penalty (3 posts/dia IA)
6. **Risco exógeno macro** — Meta WhatsApp Channels regra (DC41 portabilidade Telegram) · LLM citation favorites mudando (DC50 GEO/AEO janela 12-18m)

Output integrado em `<marca>-propagacao-campo-de-batalha.md` (seção "Risk Audit") OU arquivo separado `meu-risks-audit.md` (decisão do aluno).

---

## Modo 6.5 · Pre-Launch Asset Manifest (CONDICIONAL · Ganho #6 absorvido)

**Dispara APENAS quando aluno declara marco data-fixa** (ex: "lançar Forja Alma V1 em D+90" · "evento Mackenzie 2027"). Para campanha always-on (Hub-Spoke contínuo), pular este modo.

**Função canon:** listagem EXAUSTIVA de assets pré-launch · não derivados de Hub (que são as 16 tasks SPK-XXX) · mas **assets fundacionais necessários ANTES da campanha começar**.

**Categorização canônica:**

| Asset | Tipo | Prioridade canon | Production timeline |
|---|---|---|---|
| Landing page produto | LP | must-have | 5-7d |
| Comparison page (X vs Y) | LP | must-have B2B (DC49 comitê) | 5-7d |
| Welcome sequence pós-compra | Email/Stack v2.0 | must-have | 5-10d (4 sequences canon DC58) |
| Pillar Blog tese central | Blog 3.000+p (DC57) | must-have (Hub canon SPK-001) | 5-10d |
| Vídeo lançamento (Cold Open + BENS) | YouTube + cross-channel | must-have (DC48) | 2-4sem |
| 16 tasks SPK-XXX Hub-Spoke aquecimento | Distribuídas Sem 1-6 | must-have | Conforme stagger |
| Carrosséis depoimentos beta | IG/LinkedIn PDF | nice-to-have | 2-3d/peça |
| Régua 14d WhatsApp Channel | Stack v2.0 N8N (4 toques DC58) | must-have BR | 5-10d setup |
| Stripe checkout + zero-party | Site | must-have | (feito #95+#112-114) |
| Dashboard métricas-âncora | Admin WP | must-have | (feito #72) |

**Output:** `meu-pre-launch-manifest.md` com lista priorizada must-have/nice-to-have + timeline reversa.

**Anti-padrão canon:**
- ❌ Marco data-fixa sem manifest = sem-controle
- ❌ Manifest 100% must-have = inflexível (20% flex obrigatório · canon NotebookLM)
- ❌ Manifest ignorando production timeline = fadiga + qualidade ruim

**Exemplo (lançamento de um produto digital, D+90):**
- D-40 (start): pillar Blog tese (5-10d produção)
- D-42 (start): vídeo lançamento BENS (2-4sem)
- D-28 (start): página de venda do produto (5-7d)
- D-14: SPK aquecimento intensivo
- D+0 (23/Ago): launch
- D+0-7: welcome sequence rodando
- D+14: 1ª venda externa target

Cross-ref: skill `marketing:campaign-plan` §Content Pieces Needed (absorvida 2026-05-25).
