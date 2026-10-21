# Continuidade entre sessões · Modo 0.5 + Modo 0.6

> **Ler QUANDO:** no início de qualquer sessão, se o glob de Forjas anteriores encontrar ≥1 `forja-state.json` (Modo 0.5) — e sempre que o usuário escolher rodar uma 2ª+ Forja na mesma empresa (Modo 0.6). Se nenhuma Forja anterior existe, este arquivo não é necessário: vá direto ao Passo 0 (Setup).

---

## Modo 0.5 · Orientação Inicial (automático se Forja anterior existe · EXPANDIDO V1.5)

**Quando ativar:** ao iniciar qualquer sessão, fazer 2 buscas:

1. Procurar `marca/.forja-state-estrategia.json` e os arquivos `forja-plano-*`, `forja-diagnostico-*` e `forja-educacao-*` na pasta `marca/` da marca em uso (ver `${CLAUDE_PLUGIN_ROOT}/skills/_comum/pasta-marca.md` e `${CLAUDE_PLUGIN_ROOT}/skills/_comum/retomada.md`)
2. Se encontrou ≥1 state.json, identificar qual sessão é relevante pro contexto atual (= mesma empresa? mesma disciplina? data mais recente?)

**🆕 V1.5 · LEITURA OBRIGATÓRIA DE 4 ARQUIVOS (= cicatriz #6 captura)**

Quando Forja anterior identificada como relevante · **ler TODOS os 4 arquivos canon**, não só state.json:

```
marca/
  ├── forja-plano-<slug>-<disciplina>-<data>.md       (= riqueza executiva · marcos · cadência)
  ├── forja-diagnostico-<slug>-<disciplina>-<data>.md (= descobertas + cicatrizes + chunks)
  ├── forja-educacao-<slug>-<disciplina>-<data>.md    (= conceitos + frameworks operacionais)
  └── .forja-state-estrategia.json                    (= resumo estruturado)
```

**Anti-padrão V1.4 (cicatriz #6, 2026-05-23):** ler só o estado salvo da Forja anterior perde tudo o que formou aquela Forja; carregar todos os arquivos dela.

state.json é **resumo estruturado** · NÃO substitui a leitura completa dos 3 .md. Ler só state = começar próxima Forja com 60% do canon visível.

**Após ler os 4 · apresentar briefing de retomada (5-8 linhas):**

```
═══════════════════════════════════════════
RETOMANDO/CONTINUANDO FORJA · <empresa>
═══════════════════════════════════════════
Forja anterior: <disciplina> · <data>
4 arquivos canon lidos: ✅ plano · ✅ diagnóstico · ✅ educação · ✅ state

Tese estratégica anterior:
"<frase>"

3 descobertas canon foundational anteriores:
- <descoberta 1>
- <descoberta 2>
- <descoberta 3>

3 cicatrizes strategist registradas:
- <cicatriz 1>
- <cicatriz 2>
- <cicatriz 3>

Opções:
A) Retomar Forja anterior (= mesma empresa · mesma disciplina · continuar de P<N>)
B) Nova Forja mesma empresa (= disciplina diferente · Modo 0.6 enxuto)
C) Forja nova empresa (= setup do zero)
═══════════════════════════════════════════
```

Aguardar escolha do usuário. Não presumir.

**Se nenhuma Forja anterior existe:** prosseguir diretamente ao Passo 0 (Setup).

---

## Modo 0.6 · Cross-Forja Consume (= 2ª+ Forja na mesma empresa · NOVO V1.5)

**Quando ativar:** Usuário escolheu opção B no Modo 0.5 (= mesma empresa · disciplina diferente).

**Princípio canon:** empresa já documentada NÃO precisa re-fazer P1-P3 (empresa/setor/ICP) · só perguntar o que é **específico da nova disciplina**.

**Procedimento:**

1. **Identificar campos REUTILIZÁVEIS** do state.json anterior:
   - `empresa.nome` · `empresa.setor` · `empresa.porte` · `empresa.tese_missao_canon` · `empresa.identity_stack_canon` · `empresa.icp_principal` · `empresa.icp_secundario`
   - `named_entities_ledger` (= ledger completo · pessoas/clientes/concorrentes)
   - `alma_canon_anexa`
   - `cicatrizes_canon_strategist_REGISTRADAS` (= não apagar · acumular)

2. **Identificar perguntas ESPECÍFICAS da nova disciplina** (= pular 12 estações canon · gerar 4-8 perguntas focadas):
   - Cada disciplina tem set de perguntas próprio (ver § Disciplina-specific question sets abaixo)
   - Default: 5-8 perguntas mais enxutas que cobrem o vocabulário canônico da disciplina

3. **Apresentar briefing curto** mostrando:
   - O que vai REUTILIZAR (= 5-8 linhas)
   - Quais perguntas ESPECÍFICAS da disciplina vão ser feitas
   - Pedir confirmação antes de prosseguir

4. **Conduzir entrevista enxuta** (= ritmo conversa mantido · uma por vez · maiêutico)

5. **State.json desta nova Forja** marca campos REUTILIZADOS com sufixo `_REUTILIZADO_forja_anterior` (= Hard Rule #10 canon V1.5 · cf `hard-rules-precisao.md §Hard Rule #10`)

**Exemplo canon 2026-05-23 (Forja Comunicação Integrada):** 6 perguntas PC1-PC6 focadas (cadência canais · Hybrid Attribution · PESO Model · régua de relacionamento · SHIFT TECH STACK newsletter · movimento 30d). Tempo total: ~30 min vs 45-60 min full canon.

**Disciplina-specific question sets (= placeholder para V1.6 expansão):**

- **Comunicação Integrada (Cat 2)**: cadência canais · atribuição · PESO · régua · stack tech · movimento 30d
- **Growth & Performance (Cat 3)**: funnel atual · CAC/LTV · canais Paid · MMM readiness · north star metric · movimento 30d
- **Estratégia & Posicionamento (Cat 1)**: 12 estações canon completas (= disciplina foundational · default)
- **IA & MarTech (Cat 7)**: stack atual IA · workflows · time AI literacy · skills construídas/compradas · governança · movimento 30d
- *(outras disciplinas: V1.6 expansão · por enquanto fallback 12 estações canon)*
