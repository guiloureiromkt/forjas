# Hard Rules de Precisão · canon obrigatório no Modo Diagnóstico

> **Origem:** teste real da V1.1 com uma agência, em 2026-05-20. A skill confundiu nomes · sintetizou afirmações que o usuário não fez · fundiu 2 achados em 1 anti-padrão com cadeia causal frouxa.
> **Status:** canon hard 2026-05-20 · bloqueia emissão de Chunk até checklist passar.

---

## Hard Rule #1 · Re-cita literal antes de descrever

Antes de afirmar que o usuário disse X, RE-CITAR o trecho literal entre aspas (do state.json ou da transcrição). Se a citação não existe textualmente, NÃO afirmar.

**Aplica em todo Chunk** (não só Chunk 2 · Diagnóstico inteiro).

**Implementação prática:** cada anti-padrão de Chunk começa com:

```markdown
> "citação literal do usuário"

**O que está acontecendo:** [descrição ancorada na citação]
```

Sem citação literal · não emitir o ponto.

---

## Hard Rule #2 · Um achado · um anti-padrão · proibido fundir 2

Se uma seção combina 2 achados distintos do state, FORÇAR separação em 2 anti-padrões — mesmo que fique mais comprido.

**Por que:** synthesis overreach é tentação porque parece mais punchy. Mas custa precisão e o usuário não consegue contestar pontualmente.

**Detecção automática (auto-check antes de emitir):** se na descrição do anti-padrão aparecer mais de 2 entidades de Estação diferentes sem cadeia causal explícita · REVISAR e SEPARAR.

**Exemplo do que NÃO fazer:**
> "Vocês têm last-click + tensão marketing vs vendas + briefing genérico do CEO = sistema operando refém de métrica obsoleta."

**Exemplo do que FAZER:**
> Anti-padrão 1 · Last-click (com citação P5)
> Anti-padrão 2 · Tensão marketing vs vendas (com citação P7)
> Anti-padrão 3 · Briefing genérico (com citação P6)
> [Conexão entre eles vai numa seção separada de "padrões cruzados" · se houver]

---

## Hard Rule #3 · Ledger de entidades nomeadas · consulta obrigatória

Adicionar bloco fixo ao `state.json` durante a Entrevista:

```json
"named_entities_ledger": {
  "pessoas_dentro_empresa": {
    "Nome A": "função · contexto",
    "Nome B": "função · contexto"
  },
  "pessoas_externas": {
    "Nome X": "função/relação com a empresa",
    "Nome Y": "..."
  },
  "concorrentes": ["..."],
  "clientes_atuais": ["..."],
  "fornecedores": ["..."]
}
```

**Hard rule de uso:** antes de mencionar QUALQUER nome próprio no Diagnóstico ou outputs, CONSULTAR o ledger.
- Se o nome existe no ledger · usar com a função/contexto correta
- Se NÃO existe · NÃO mencionar nem inventar. Pedir confirmação ao usuário primeiro.

**Captura do ledger:** durante a Entrevista (especialmente Estações 2, 8, 11, 11.5, 12 que tendem a trazer nomes), incrementar o ledger a cada resposta.

### Exemplo preenchido (caso inventado · referência de calibragem)

```json
"named_entities_ledger": {
  "pessoas_dentro_empresa": {
    "Marta Ribeiro": "CEO · sócia fundadora",
    "Jonas": "sócio · diretor de operações",
    "Bia Torres": "diretora de criação",
    "Rui": "diretor de atendimento",
    "Usuário desta sessão": "diretor de estratégia"
  },
  "pessoas_externas": {
    "Secretária de Comunicação": "cliente B2G (prefeitura) · nome a confirmar"
  },
  "concorrentes": ["Agência X", "Agência Y"],
  "clientes_atuais": ["Prefeitura Z", "Cliente B", "Cliente C"],
  "fornecedores": ["Fornecedor de mídia A"]
}
```

**Como usar o exemplo:** durante a Entrevista, o agente preenche o ledger com nomes REAIS que o usuário trouxer. Se o usuário disser "meu CEO" sem nomear · capturar como `"CEO": "função · não nomeado"` e perguntar nome opcionalmente. Se mencionar concorrente sem detalhar · capturar com `"Nome": "concorrente · contexto a confirmar"`.

**Anti-padrão:** inventar "João" ou "Maria" como exemplo no Diagnóstico se esses nomes não estão no ledger. Resultado de teste real (2026-05-20): Claude mencionou nomes que o usuário não tinha trazido · quebra de confiança imediata.

---

## Hard Rule #4 · Fact-check pass antes de emitir Chunk

Pseudo-checklist auto-executável a rodar mentalmente ANTES de enviar cada Chunk do Diagnóstico:

1. **Toda citação direta entre aspas está no transcript?** Se não · remover ou parafrasear sem aspas.
2. **Todo nome próprio está no ledger?** Se não · refatorar pra remover ou pedir confirmação.
3. **Toda afirmação "você disse X" tem trecho literal correspondente?** Se não · refatorar.
4. **Toda síntese de mais de 2 Estações tem cadeia causal explícita OU foi separada em pontos distintos?** Se não · separar.
5. **Cada ponto segue O QUE · POR QUE · O QUE FAZER?** Se não · completar.
6. **Nenhuma menção a "corpus" · "canon" · "cânone" · "sub-tese" · "anchor quote" · "anti-corpus" · "tríade" · "modo maiêutico" user-facing?** Se sim · substituir por linguagem leiga.

Se QUALQUER check falhar · NÃO emitir o Chunk até corrigir.

---

## Hard Rule #5 (novo · 2026-05-20) · Pesquisa Externa antes do Diagnóstico

Feedback do autor, depois de um teste: "faltou pesquisa, faltou questionar se o que eu estava direcionando era ruim, ou eu posso ser só bom mesmo. Essa skill se beneficiaria demais de uma deep research de base."

Adicionar **Modo 1.5 · Pesquisa Externa** entre Entrevista e Diagnóstico. Ver `SKILL.md §Modo 1.5`.

A Forja não pode apoiar 100% no que o usuário disse · senão vira eco-câmara cara. Antes do Diagnóstico, sempre rodar pesquisa externa:
- Concorrentes nomeados (Estação 8) — verificar o que de fato fazem hoje (não o que usuário acha que fazem)
- Tendências do setor da empresa (Estação 1)
- Cases recentes (últimos 18 meses) da disciplina escolhida no setor da empresa
- Público-alvo · dores reais documentadas (não as que usuário projetou)

**Como rodar:** se ambiente tem skill `deep-research` instalada · invocar com briefing contextual. Se não · fallback para Exa MCP · WebSearch · ou pedir ao usuário pra fornecer 3-5 links de referência.

**Anti-padrão a evitar:** Diagnóstico baseado SÓ no state.json (perspectiva do usuário). Sempre cruzar com 1 fonte externa minimamente.

---

## Aplicação prática do Fact-check Pass

Antes de emitir cada Chunk · o agente deve rodar mentalmente:

```
[ ] Chunk N de 4 (qual?)
[ ] Citações literais conferidas no state.json (lista quais)
[ ] Nomes próprios conferidos no ledger (lista quais)
[ ] Afirmações "você disse" têm trecho literal (lista quais)
[ ] Sínteses de 2+ Estações têm cadeia causal explícita OU foram separadas
[ ] Padrão O QUE · POR QUE · O QUE FAZER aplicado em cada ponto
[ ] Linguagem leiga · zero "corpus/canon/cânone/sub-tese/etc."
[ ] Pesquisa externa cruzada com afirmações do Chunk (links/fontes citadas)
```

Se algum check falhar · refatorar antes de enviar.

---

# Hard Rules #6-#13 (V1.4-V1.6 · consolidadas aqui em 2026-07-13)

> Origem: viviam no SKILL.md; movidas pra cá na reestruturação progressive disclosure. O SKILL.md mantém a lista resumida de 1 linha por regra.

## Hard Rule #6 · Ponta final obrigatória (V1.4)

Todo canal de captura descrito no forja-plano.md deve nomear o produto destino específico (por exemplo: o e-book X, a mentoria Y, a consultoria Z · nunca genérico "conteúdo" ou "lead"). Ação sem destino concreto é retirada do plano antes de salvar.

## Hard Rule #7 · Siglas explicadas na 1ª aparição (V1.4)

Todo termo técnico ou sigla (ICP, JTBD, PESO, MMM, ROI, CAC, LTV, ROAS, NPS, B2B, B2C, Dark Social, GEO, etc.) aparece como `SIGLA (= significado completo)` na primeira ocorrência em qualquer chunk ou documento. Nunca presumir que o usuário conhece o acrônimo.

## Hard Rule #8 · Bias anti-status-quo em stack tecnológico (V1.4)

Quando detectar ferramenta ou canal estagnado há mais de 12 meses sem resultado documentado, oferecer SUBSTITUIÇÃO DE STACK como 1ª opção no Chunk 2 ou 3. Opções conservadoras (kill/hibernate/aguardar dentro do mesmo stack) só depois de explorar alternativas reais. Princípio: stack travado é problema de modelo, não de execução.

## Hard Rule #9 · Glossário canon obrigatório no Manual Educativo (V1.5)

Todo `forja-educacao.md` começa com seção **"Vocabulário canon"** consolidando TODAS as siglas usadas no manual em tabela `| Sigla | Significado completo |`. Hard Rule #7 (explicar siglas na 1ª aparição) é diretiva inline · esta é repositório de referência. Time futuro que ler o manual precisa de glossário centralizado · não 21 explicações espalhadas.

## Hard Rule #10 · Cross-Forja state continuity schema (V1.5)

Quando 2ª+ Forja na mesma empresa (= Modo 0.6 ativado) · campos REUTILIZADOS do state.json anterior recebem sufixo `_REUTILIZADO_forja_anterior` no novo state.json. Garante: rastreabilidade do que foi recarregado vs descoberto nesta sessão · evita stale data sendo tratado como current · facilita auditoria entre Forjas. Aplicado já na sessão 2026-05-23 Cat 2 Comunicação Integrada. Procedimento completo: `continuidade-cross-forja.md`.

## Hard Rule #11 · Obrigação de propagar (protocolo em `${CLAUDE_PLUGIN_ROOT}/skills/_comum/propagacao.md`)

Forja DEVE ler o que já existe (o Master Brief, os arquivos da pasta `marca/` de Forjas anteriores, o material que a pessoa apontar e o `CLAUDE.md` da pasta, se houver) **E** gerar o arquivo de propagação (descobertas × onde precisam chegar · plano P0/P1/P2/P3 · pendências). Skill que termina sem esse arquivo está INCOMPLETA. Cicatriz que originou a regra: uma Forja depositou 30 descobertas numa pasta e não propagou; durante 48-72h o material da marca e as skills de produção trabalharam com a versão antiga.

## Hard Rule #12 · Foundational Cascade (V1.6)

Forja da Alma é foundational. Suas descobertas (UVP · arquétipos · tese · anti-claims · princípios · ICP · voz · inimigos) DEVEM ser carregadas como input por TODAS as Forjas posteriores via Modo 0.5 estendido. Forjas posteriores NUNCA podem criar canon de identidade/voz/inimigos em paralelo — só consomem e estendem. Output do Modo 0.5 declara explicitamente "li N arquivos canon prévio · M descobertas Forja Alma carregadas". Se Forja Alma não existe ainda · sinalizar gap antes de seguir.

## Hard Rule #13 · Output Sink No More (V1.6)

Forja NÃO é skill de "produzir 3-4 .md no disco". Forja é skill de "propagar N descobertas canon pelo ecossistema". Ao terminar Modo 5 (entrega dos 4 .md + state.json) · disparar AUTOMATICAMENTE **Modo 6 · Propagação** (não-opcional · protocolo em `${CLAUDE_PLUGIN_ROOT}/skills/_comum/propagacao.md` · operação em `modo-6-propagacao.md`). Modo 6 pergunta ao usuário "Quer propagação agora ou registramos pra próxima sessão?". Se "depois" · registrar a pendência na §6 do Master Brief. **Forja só é considerada COMPLETA quando propagação aconteceu (não quando 4 .md foram salvos).**
