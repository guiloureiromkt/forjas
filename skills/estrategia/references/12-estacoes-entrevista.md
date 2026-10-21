# 12 Perguntas · Modo Entrevista da Forja

> **Como funciona:** uma pergunta por vez. Aguarda resposta. Confirma entendimento em 1 frase. Próxima.
>
> **Tom:** conversa de consultor sênior com cliente de respeito. Não interroga. Não despeja lista. Não usa jargão sem explicar.
>
> **Hard rule:** se o usuário responder de forma vaga · refraseie a pergunta pedindo dado concreto (empresa + número + data). Se ele resistir 2x · seguir mesmo assim e marcar no estado: `dado_ancorado: false` (vai limitar o diagnóstico depois).

---

## Pergunta 1 · A Empresa em 3 Frases

**Pergunte:** "Conta pra mim sobre sua empresa em 3 frases. Quem é · o que faz · pra quem. Não quero brochura · quero a versão que você daria pra um colega num jantar."

**Por que essa pergunta:** verifica se o usuário tem clareza articulável. Resposta de brochura ("somos líderes em soluções inovadoras...") é sinal vermelho. Se vier vaga · pedir o NÚMERO concreto que mostra que ele faz isso bem.

**Capturar:** `empresa.nome` · `empresa.setor` · `empresa.descricao_curta`

---

## Pergunta 2 · O Cliente Real (vs o que ele Acha Que é)

**Pergunte:** "Quem é o cliente que paga MELHOR · que tem MENOR custo de aquisição · que recomenda MAIS? Não o cliente ideal de pitch deck — o REAL que você teve nos últimos 12 meses. Me dá 1-2 exemplos com setor · porte · ticket · custo de aquisição aproximado."

**Por que essa pergunta:** o cliente declarado e o cliente real raramente batem. Quem responde rápido com dado concreto = tem visão de dado próprio. Quem hesita = opera no instinto. Essa diferença vai aparecer fortemente no diagnóstico depois.

**Capturar:** `empresa.icp_declarado` · `empresa.icp_real` · `empresa.icp_examples`

---

## Pergunta 3 · A Jornada Que Você Acha Que Existe

**Pergunte:** "Do momento que alguém ouve falar de vocês pela primeira vez até virar cliente · me descreve a jornada como VOCÊ acredita que ela acontece. Pontos de contato · canais · tempo médio · quem (qual persona) descobre vocês onde."

**Por que essa pergunta:** captura o modelo mental do usuário. Vai bater com a realidade ou divergir? Quando diverge = gap importante de diagnóstico. Especialmente revelador em B2B onde a jornada quase sempre tem partes invisíveis (conversa no WhatsApp · indicação no almoço).

**Capturar:** `empresa.jornada_declarada`

---

## Pergunta 4 · A Stack Real (vs Stack do PowerPoint)

**Pergunte:** "Lista TUDO que vocês usam em comunicação · marketing · IA · análise. Não me dá o ideal — me dá o REAL. CRM · ferramentas de mídia · plataformas de email · ferramentas de IA · dashboards. Tudo. Inclusive aquela que 'pra falar a verdade ninguém abre mais'."

**Por que essa pergunta:** stack inchada sem uso = caos. Stack minimalista funcional = sistema. Revela maturidade operacional real. Também revela quais investimentos foram feitos mas não geraram retorno.

**Capturar:** `empresa.stack_atual` (separar em 3 grupos: muito uso · uso médio · comprou e abandonou)

---

## Pergunta 5 · A Métrica Que Manda

**Pergunte:** "Qual é a UMA métrica que · se cair pela metade · você é demitido no mês seguinte? E qual é a métrica que · se subir 30% · você ganha bônus? Não responda 'depende' · responda em 1 frase cada."

**Por que essa pergunta:** revela accountability real. CMOs que respondem "ROI" sem detalhar = não têm número específico. Quem responde "MQL pra SQL conversão segmento varejo" = tem sistema. Essa pergunta vai mostrar se a métrica que define carreira tá alinhada com prática moderna ou refém de modelos obsoletos (last-click etc.).

**Capturar:** `empresa.metrica_demite` · `empresa.metrica_bonifica` · `empresa.atribuicao_atual`

---

## Pergunta 6 · O Briefing Que Você Mais Recebe

**Pergunte:** "Qual o briefing que você mais recebe? Da diretoria · de cliente · de board. Em 1 frase. Algo tipo 'aumenta o ROAS' ou 'precisamos viralizar' ou 'cliente quer marca mais jovem'. Me dá o briefing REAL · não o briefing curado."

**Por que essa pergunta:** briefing real revela onde o sistema falha. Briefing genérico ("precisamos ser mais reconhecidos") = falta de Alma da Marca documentada. Briefing específico ("aumentar conversão MQL→SQL no segmento varejo de 12% pra 18% no Q3") = sistema saudável.

**Capturar:** `empresa.briefing_recorrente`

---

## Pergunta 7 · A Tensão Que Não Resolve

**Pergunte:** "Tem alguma tensão dentro da empresa que volta toda reunião e nunca resolve? Pode ser entre departamentos (marketing vs vendas · marketing vs produto) · entre níveis (diretoria vs operação) · entre canais (orgânico vs paid). Me descreve a TENSÃO REAL · em 2-3 frases · com exemplo concreto."

**Por que essa pergunta:** tensões estruturais revelam onde a Alma da Marca está fraca. Quase toda empresa tem 1-2 tensões clássicas (marketing vs vendas é a mais comum) · mas a forma como ela se manifesta nessa empresa específica vai ditar o diagnóstico.

**Capturar:** `empresa.tensao_estrutural`

---

## Pergunta 8 · O Concorrente Que Te Tira O Sono

**Pergunte:** "Qual concorrente · player · creator · agência · ou marca te incomoda? Não diz 'todos' · diz 1-2 nomes específicos. E me diz POR QUE. O que eles fazem que você não consegue · ou faz pior?"

**Por que essa pergunta:** concorrente nomeado = mercado mapeado. "Todos" = falta de visão competitiva clara. O que admiram nos outros mostra qual área específica precisa de evolução.

**Capturar:** `empresa.concorrentes_nomeados` · `empresa.diferencial_inveja`

---

## Pergunta 9 · O Que Já Tentou E Não Funcionou

**Pergunte:** "Me conta 2-3 coisas que vocês JÁ tentaram em comunicação/marketing/IA nos últimos 12 meses · e que NÃO funcionaram. Não me peça desculpas · não justifique · só me conta o que tentou · quanto custou · e por que você acha que não rolou."

**Por que essa pergunta:** revela apetite a risco · capacidade de autodiagnóstico · honestidade. Quem responde sem hesitar = profissional sênior real. Quem evita = imaturo ou cosmético. Crítico pra diferenciar erros já testados (não repetir) de gaps reais (oportunidade).

**Capturar:** `empresa.tentativas_falhas` (lista: descrição · custo · razão)

---

## Pergunta 10 · A Hipótese Atual

**Pergunte:** "Se você fechasse uma promessa de bônus de R$ 100 mil pelo próximo trimestre · em que UMA aposta estratégica você colocaria essa grana? Não diga 'depende' · diga uma. Pode ser 'investir em otimização pra IA antes que ChatGPT mude o tráfego' ou 'parar Meta Ads e investir em newsletter própria' ou 'contratar 3 estrategistas e demitir 5 freelas'. Uma."

**Por que essa pergunta:** força priorização. Quem tem hipótese clara = visão de mundo. Quem responde 'depende' = falta de tese. A hipótese vai ser cruzada com o material da biblioteca · diagnóstico vai mostrar se ela ressoa com estado-da-arte ou se vai dar errado.

**Capturar:** `empresa.hipotese_estrategica`

---

## Pergunta 11 · O Time Real

**Pergunte:** "Quantas pessoas no time de marketing/comunicação? Quantas seniores · plenas · juniores · freelas? Você inclui? Quem REPORTA pra quem? E qual é a função do time que você acha que é a mais SUBVALORIZADA por você mesmo?"

**Por que essa pergunta:** captura realidade operacional. Time grande sem clareza de função = caos. Time pequeno multifuncional = sistema enxuto. A autocrítica sobre função subvalorizada revela onde está o gap interno.

**Capturar:** `empresa.time_estrutura` · `empresa.time_funcao_subvalorizada`

---

## Pergunta 11.5 · O Interlocutor Principal (adicionada 2026-05-20 · feedback do autor)

**Pergunte:** "Quando você tem que VENDER alguma coisa nova internamente — uma ferramenta · uma mudança de estratégia · um corte de canal — quem é o INTERLOCUTOR PRINCIPAL que você precisa convencer? Não me diga 'a diretoria'. Me diga em 1-2 frases: nome ou função · idade aproximada · perfil (técnico · político · cético · entusiasta) · qual a referência intelectual dele (lê o que · escuta o que · admira quem). Se houver 2 interlocutores · me dá os 2."

**Por que essa pergunta:** o decisor real molda o formato do Plano final. Diretor financeiro cético quer planilha + cenários · CEO entusiasta quer narrativa + visão · sócio operacional quer milestone semanal. Plano genérico não vende internamente · plano calibrado pro interlocutor SIM.

**Capturar no state.json:**
- `empresa.interlocutores_principais[]` (array)
  - `nome_ou_funcao`
  - `idade_aprox`
  - `perfil` (técnico · político · cético · entusiasta · misto)
  - `referencia_intelectual` (o que lê · escuta · admira)

**Capturar TAMBÉM no `named_entities_ledger`** (cf `hard-rules-precisao.md §Hard Rule #3`).

---

## Pergunta 12 · O Próximo Movimento Forçado

**Pergunte:** "Se você tivesse que entregar UM plano em 30 dias pro seu chefe/board/cliente · e esse plano tinha que mostrar evolução real e não cosmética · qual seria o primeiro movimento que VOCÊ tomaria? Não 'a empresa deveria' — VOCÊ. Em 1 frase ou 2."

**Por que essa pergunta:** captura agência real do usuário. Quem responde com movimento próprio = profissional ativo. Quem espera "a diretoria decidir" = passivo. O primeiro movimento dele vai abrir o documento de Plano (Modo Entrega) — vai virar prioridade #1 das primeiras 2 semanas.

**Capturar:** `empresa.movimento_30_dias`

---

## Checkpoint após Pergunta 12

Antes de partir pro Modo Diagnóstico:

1. **Mostre o resumo** das 12 respostas em formato humano-legível (tabela ou bullets)
2. **Pergunte:** "Bate com sua realidade? Algo pra ajustar antes de eu cruzar com a biblioteca de [disciplina]?"
3. Se usuário ajustar · atualize `state.json`
4. **Confirme:** "Vou agora cruzar suas respostas com a biblioteca de [disciplina]. Vou te entregar em 4 partes (o que vocês fazem bem · o que tá errado · gaps · oportunidades) · cada uma com explicação do porquê. Demora ~3-5 minutos. Posso seguir?"

---

## Variações por disciplina (V2 · expansão futura)

V1 entrega 12 perguntas padrão otimizadas pra Comunicação Integrada e disciplinas correlatas. V2 vai trazer variações específicas:

- **Estratégia & Posicionamento:** P8 (concorrente) vira "Categoria onde você compete · quem define padrão"
- **Growth & Performance:** P5 (métrica) vira "Funil AAARRR · qual etapa vaza mais"
- **Sistemas de Marca:** P4 (stack) vira "Onde mora seu padrão de marca · quem mantém · quem audita"
- **Dados & Inteligência:** P5+P6 viram bloco único "Stack de dados + atribuição atual"
- **IA & MarTech:** P4 vira "Quais ferramentas de IA em produção · com qual fluxo de trabalho"
- **Experiência & Ativação:** P3 (jornada) vira "Pontos de contato presenciais/digitais · qual ativação foi mais memorável"
- **Cultura & Ciclos:** P8 vira "Que ciclo de marketing você está vivendo e ainda não nomeou"
