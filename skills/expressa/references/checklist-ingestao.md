# Checklist de Ingestão · o que extrair da base (Modo 1)

> **Quando ler:** SEMPRE antes de começar a ler a base do cliente. Este arquivo é a tradução das entrevistas das Forjas-mãe (12+1 perguntas da Estratégia + briefing 7-campos do Campo de Batalha) pra modo LEITURA: cada campo diz onde procurar numa base típica e qual pergunta fazer se faltar.
>
> **Disciplina de extração (Hard Rule #1 herdada):** campo só conta como PREENCHIDO com citação literal + arquivo de origem. Paráfrase sem fonte = gap. Toda entidade nomeada encontrada entra no ledger com tag INTERNO/EXTERNO/CLIENTE/CONCORRENTE.

---

## Bloco A · Negócio & Estratégia (13 campos · espelho da entrevista 12+1)

| # | Campo (state.json) | Vital? | Onde procurar na base | Armadilha de leitura | Pergunta de gap (se faltar) |
|---|---|---|---|---|---|
| 1 | `empresa.descricao_curta` (+nome +setor) | ✅ | Site/about · brand system · Master Brief §1 · propostas | Texto de brochura ("líderes em soluções...") preenche o campo mas marcar `tom: brochura` — pedir no lote a versão de jantar | "Em 3 frases · sem brochura: quem são · o que fazem · pra quem?" |
| 2 | `empresa.icp_real` (vs `icp_declarado`) | ✅ | Cases com nome · depoimentos · propostas fechadas · CRM/relatório comercial | A base quase sempre documenta o ICP DECLARADO. ICP real precisa de EVIDÊNCIA (cliente que pagou · ticket · recompra). Se só há o declarado → preencher `icp_declarado` e perguntar o real | "Quem foi o cliente que pagou melhor · custou menos pra adquirir e mais indicou nos últimos 12 meses? 1-2 exemplos com setor · porte · ticket" |
| 3 | `empresa.jornada_declarada` | — | Playbook de vendas · funil documentado · mapa de jornada | Jornada B2B tem partes invisíveis (WhatsApp · indicação) que doc nenhum registra — anotar como suspeita pro diagnóstico | "Do primeiro contato até virar cliente: canais · tempo médio · onde cada persona descobre vocês?" |
| 4 | `empresa.stack_atual` (3 grupos: muito uso · médio · abandonado) | — | Docs de ferramentas · integrações · faturas/contratos de SaaS | Base NUNCA confessa "compramos e ninguém abre". Extrair a lista e perguntar no lote só o grupo abandonado | "Dessa stack que encontrei [listar] · qual ferramenta ninguém abre mais?" |
| 5 | `empresa.metrica_demite` + `metrica_bonifica` + `atribuicao_atual` | ✅ | OKRs · dashboards · relatórios de resultado · apresentações de board | Relatório mostra MÉTRICAS ACOMPANHADAS · não a que define carreira. Se houver várias sem hierarquia → gap | "Qual métrica · se cair pela metade · te demite? E qual · se subir 30% · te bonifica? 1 frase cada" |
| 6 | `empresa.briefing_recorrente` | — | Atas · e-mails de diretoria · briefings arquivados | Briefing curado ≠ briefing real. Se só há versões polidas → gap | "Qual o pedido que mais chega da diretoria/cliente · na frase REAL em que ele chega?" |
| 7 | `empresa.tensao_estrutural` | — | Quase NUNCA documentada | Não perder tempo caçando · é pergunta padrão do lote | "Qual tensão volta toda reunião e nunca resolve (marketing×vendas · diretoria×operação · orgânico×paid)? 2-3 frases com exemplo" |
| 8 | `empresa.concorrentes_nomeados` + `diferencial_inveja` | ✅ | Análise competitiva · decks de posicionamento · propostas (seção "diferenciais") | Se a base não nomeia ninguém · a pesquisa externa (Modo 1.5) NOMEIA candidatos e o cliente confirma no lote — não aceitar "todos" | "Qual 1-2 concorrentes te incomodam · e o que eles fazem que vocês não conseguem?" |
| 9 | `empresa.tentativas_falhas` | — | Post-mortems · retrospectivas (raro) | Empresa documenta vitória · não derrota. Pergunta quase sempre vai pro lote | "2-3 coisas que tentaram nos últimos 12 meses e NÃO funcionaram: o que · quanto custou · por quê" |
| 10 | `empresa.hipotese_estrategica` | ✅ | Planejamento vigente · OKRs do tri · última apresentação de estratégia | Planejamento lista 10 apostas = não tem hipótese. Forçar UMA no lote se necessário | "Se tivesse que apostar o bônus do trimestre numa ÚNICA aposta estratégica · qual seria?" |
| 11 | `empresa.time_estrutura` + `time_funcao_subvalorizada` | — | Organograma · página de time · contratos com agências/freelas | Organograma dá estrutura · não dá a autocrítica (função subvalorizada) — meio a meio | "Quem faz marketing hoje (sênior/pleno/júnior/freela · quem reporta a quem)? E qual função VOCÊ mesmo subvaloriza?" |
| 11.5 | `empresa.interlocutores_principais[]` (nome/função · idade aprox · perfil · referência intelectual) | ✅ | Quase NUNCA documentado | Pergunta padrão do lote — molda o FORMATO do plano final (financeiro cético = cenários · CEO entusiasta = narrativa · operacional = marcos) | "Quando você vende uma ideia nova internamente · quem precisa convencer? Função · perfil (técnico/político/cético/entusiasta) · o que essa pessoa lê/admira" |
| 12 | `empresa.movimento_30_dias` | ✅ | NUNCA documentado (é agência pessoal · não doc) | Pergunta padrão do lote — abre o plano como prioridade #1 | "Se tivesse que mostrar evolução REAL em 30 dias · qual seria o SEU primeiro movimento? (você · não 'a empresa')" |

**Portão de base (Modo 1.2):** a base sozinha precisa preencher **≥8 dos 13 campos** (as perguntas 7 · 11.5 · 12 praticamente nunca vêm da base — se além delas faltarem mais de 2, a premissa "base vasta" caiu). Abaixo disso → recomendar a Forja da Estratégia completa e PARAR.

**Vitais (✅ · 6 campos):** 1 · 2 · 5 · 8 · 10 · 11.5 (+12 sempre perguntado). Nenhum vital pode entrar no diagnóstico sem resposta ancorada — vital sem resposta após o lote = marcar `dado_ancorado: false` e rebaixar a confiança do chunk que depender dele.

---

## Bloco B · Varredura de canais (comprime o briefing 7-campos)

Para **cada canal presente ou aspiracional** (LinkedIn · blog/SEO · Instagram · YouTube · WhatsApp/comunidades · site/LPs · e-mail/newsletter), capturar 4 pontos:

| Ponto | Como capturar |
|---|---|
| Existe? Estado atual | **AUDITAR olhando de verdade** (canal público não se pergunta · se abre): perfil/blog aberto no navegador ou fetch · última publicação · qualidade aparente |
| Cadência real (vs declarada) | Contar as últimas 4-8 semanas de publicação no próprio canal. Divergência doc×realidade = matéria-prima do Chunk ERRADO |
| Melhor resultado histórico COM NÚMERO | Relatórios · analytics na base · prints. Sem número na base → 1 linha no lote: "melhor resultado que você lembra em [canal] · com número" |
| Referência que admiram no canal | Raramente documentado → lote (opcional · só se sobrar espaço nas 7 perguntas) |

Registrar por canal: `canais.<canal>.{estado, cadencia_real, cadencia_declarada, melhor_resultado, referencia}` no state.json.

---

## Ordem de leitura recomendada da base

1. **Brand system / manual de marca** (se existir — também responde a Foundational Cascade: tem voz/identidade? sem isso o plano marca o gap → Forja da Alma)
2. **Master Brief** (§1 a §5.x, se existir — pula tudo que ele já responde)
3. **Planejamento/OKRs vigentes** (campos 5 · 10)
4. **Propostas comerciais + cases** (campos 1 · 2 · 8)
5. **Relatórios de resultado / analytics** (campo 5 · Bloco B)
6. **Site + canais públicos ao vivo** (Bloco B · auditoria direta)
7. **Resto do acervo** (atas · docs soltos · o que o cliente apontou)

**Anti-padrão:** ler na ordem em que os arquivos aparecem na pasta. A ordem acima existe porque os docs 1-3 criam o ledger de entidades que deixa a leitura do resto 3× mais rápida e a extração ancorada.

---

## Montagem do lote de gaps (Modo 1.2 · máx 7 perguntas)

Prioridade fixa: **vitais faltantes primeiro** (2 · 5 · 8 · 10 na prática) → **perguntas padrão** (7 · 11.5 · 12 — sempre entram) → **complementos** (4-abandonadas · 9-falhas · Bloco B números) só se sobrar slot. Passou de 7 · corta complemento, nunca vital. Formato: UMA mensagem numerada, cada pergunta com o porquê em meia linha (o cliente sênior responde melhor quando entende o uso).
