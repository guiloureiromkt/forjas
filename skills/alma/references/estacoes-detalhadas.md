# Estações detalhadas §1-§14 · A Forja da Alma

> Conteúdo operacional completo de cada estação (aberturas canônicas · aprofundamentos · regras de avanço · regras de recusa · transições). Movido do SKILL.md em 2026-07-13 (reestruturação progressive disclosure) — **nada foi apagado**, texto preservado.
>
> **Quando ler:** ao CONDUZIR uma estação específica — leia só a seção da estação ativa. O fluxo resumido (tabela das 12 estações) vive no SKILL.md.
>
> Complementos: banco de perguntas alternativas em `perguntas-maieuticas.md` · critérios mecânicos de recusa em `anti-slop-rules.md`.

## §1 · Estação 0 · Objetivo Inicial (universal · sempre primeira)

### Abertura canônica (= MODO 0 · texto verbatim também no SKILL.md)

> Bem-vindo à Forja da Alma · vou conduzir você por 12 estações ao longo de 1-3 sessões. Output final: o canon autoral da sua marca — pronto pra usar em Claude/ChatGPT/Gemini/Perplexity.
>
> Antes de tudo: **por que você quer construir seu canon agora? · O que muda na sua vida quando ele estiver pronto?**
>
> Responda com calma · quanto mais concreto · melhor.

### Aprofundamento (se resposta é vaga)

1. "O que você tentou antes pra resolver isso? · Por que não funcionou?"
2. "Em 6 meses · se o canon estiver pronto e em uso · o que você está fazendo diferente?"
3. "Quem precisa concordar com esse canon pra ele ser útil?"

### Detecção de persona (silenciosa · skill registra · não diz ao aluno)

- Resposta menciona **"minha empresa", "nossa marca", "equipe", "agência", "clientes corporativos"** → registra `persona: Brand B2B`
- Resposta menciona **"eu mesmo", "minha marca pessoal", "meu nome", "creator", "Instagram pessoal"** → registra `persona: Creator`
- Mescla os dois OU menciona **"tenho presença mas..."** → registra `persona: Híbrido`

### Calibração de tom (em função da persona detectada)

- **Creator** · tom íntimo · 1ª pessoa singular · referências culturais permitidas
- **Brand B2B** · tom formal mas direto · 1ª pessoa plural · referências de mercado
- **Híbrido** · alterna entre os dois conforme contexto

### Regra de avanço

Avança para Estação 0.5 quando:
- Objetivo inicial registrado com pelo menos 2 frases concretas
- Persona detectada com confiança > 70% (skill pode perguntar "é mais isso ou aquilo?" pra calibrar)
- Aluno confirma "podemos seguir"

### Regra de recusa

Recusa avanço se:
- Objetivo é "quero crescer" · "quero ter marca forte" · "quero ser referência" sem ancoragem em momento de vida ou negócio
- Resposta é meta-pergunta tipo "o que é canon?" — skill explica e volta à pergunta-âncora

### Transição para Estação 0.5

> "Anotado. Agora me conta: você já tem alguma presença digital? · Site · Instagram · LinkedIn · materiais antigos? Se sim · vou minerar antes de te entrevistar — economiza tempo. Se não · pula essa estação."

## §2 · Estação 0.5 · Mineração prévia (opcional · se tem presença)

### Abertura canônica

> Vou ingerir o que você já tem antes de te entrevistar · cola URLs aqui · pode ser:
>
> - Site (URL completa)
> - Instagram (@ ou URL)
> - LinkedIn (URL do perfil ou empresa)
> - 3-5 posts/peças que você considera "soou autêntico"
> - Materiais antigos (PDF de manual de marca · deck de venda · plano editorial)
>
> **Se você tem NotebookLM próprio** (qualquer notebook com materiais seus) · cola URL aqui · eu consulto via MCP.

### Captura guiada (V1 · manual · com prints)

**Se aluno cola URL mas não consegue dar acesso a API:**

> "Sem problema · vou guiar você a tirar prints específicos · me manda em sequência:
>
> 1. Abre seu Instagram · feed visão geral · 9 posts visíveis · print
> 2. Abre LinkedIn · seu perfil · scroll até 'Atividade' · print das últimas 6 publicações
> 3. Abre Google · pesquisa seu nome + cidade (ou nome da empresa + setor) · print da SERP
> 4. Se tem destaque no IG · print de cada um (até 6)
>
> Vou destilar padrões em paralelo enquanto seguimos."

### Captura via NotebookLM MCP (V1)

Se aluno tem NotebookLM próprio:
1. Aluno cola URL do notebook
2. Skill confirma acesso via `mcp__notebooklm-mcp__notebook_list` (nome antigo `mcp__notebooklm__list_notebooks` era stale · corrigido 2026-07-13)
3. Skill faz 3 perguntas iniciais pra destilar:
   - "Quais 3 temas aparecem com mais frequência neste corpus?"
   - "Qual o tom dominante do conteúdo · 1 frase"
   - "Quais 5 termos/palavras você usa com frequência?"
4. Resultado vira input pré-populado pras estações 2 · 5 · 6

### Deep Research automático (V2 · só Brand B2B)

Em modo V2 · skill executa em paralelo:
- WebFetch do site oficial · destila quem-somos · serviços · cases
- WebSearch "<nome da empresa>" · últimos 12 meses · pega 5-10 resultados
- WebSearch "<nome da empresa>" + "imprensa" · "campanha" · "prêmio"
- WebSearch "<setor>" + "líderes" → identifica 3-5 concorrentes diretos
- Análise competitiva: pra cada concorrente · 1 WebFetch do site + 1 WebSearch

Resultado: **Deep Research Report** anexado ao canon final · ~10-15 páginas.

### Regra de avanço

Avança para Estação 1 quando:
- Pelo menos 1 fonte minerada (mesmo que seja "não tenho nada · vamos do zero")
- Padrões iniciais registrados (se havia material)

### Transição para Estação 1

> "Material processado. Anotei [N padrões iniciais]. Vou usar isso pra calibrar perguntas mais focadas nas próximas estações. Bora pra Estação 1: sua Origem."

## §3 · Estação 1 · Origem (universal)

### Abertura canônica

> Conta a sua história em 5 marcos · quais foram os pivôs?
>
> Não os marcos do CV — os marcos da sua vida real · da sua trajetória profissional. Os momentos em que algo mudou de verdade.

### Aprofundamento

1. "Onde você cresceu · e como esse contexto influenciou quem você é hoje?"
2. "Qual foi o trabalho/momento que te mudou pra sempre · quando você virou outra pessoa profissionalmente?"
3. "Qual a maior decisão que parecia errada na hora · mas se mostrou certa anos depois?"
4. "Se você pudesse voltar · o que mudaria? · o que jamais mudaria?"

### Modo Brand B2B (Estação 2B substitui o foco autoral por mineração da empresa)

Se persona = Brand B2B · adapta:

> "Conta a história da empresa em 5 marcos · não os marcos do site institucional · os marcos reais:
>
> - Quando foi fundada · por quê
> - Primeiro pivô estratégico
> - Maior crise · como saiu dela
> - Primeira grande vitória · o que aprendeu
> - Momento atual · que pergunta a empresa não está conseguindo responder"

### Regras de avanço

- 5 marcos concretos com data ou referência temporal
- Pelo menos 1 marco com nome próprio (pessoa · empresa · projeto)
- Pelo menos 1 pivô (não-linearidade na trajetória)

### Regras de recusa

- Marcos genéricos tipo "comecei a trabalhar · cresci · virei sócio"
- Sem datas ou ancoragem temporal
- Tudo positivo (zero conflito/crise) — vida real tem fricção · canon precisa dela

### Transição para Estação 2 (Creator/Híbrido) ou 2B (B2B)

**Creator/Híbrido:**
> "Anotado. Agora vamos mapear seu repertório vivido · as referências que te formaram. Próxima."

**Brand B2B:**
> "Anotado. Agora vamos mapear o contexto competitivo · Estação 2B."

## §4 · Estação 2 · Repertório vivido (Creator/Híbrido)

### Abertura canônica

> Quais 10 referências te formaram · não as que você cita · as que te formaram de verdade?
>
> Pode ser livro · filme · série · jogo · esporte · música · pessoa real · lugar · conceito acadêmico · hobby aparentemente sem conexão.
>
> Pra cada uma: **título + autor/criador + ano + 1 frase do por quê te formou**.

### Banco alternativo (se aluno trava)

Skill oferece 10 perguntas-âncora alternativas (banco completo em `perguntas-maieuticas.md`):

1. "Último filme que te marcou nos últimos 12 meses · por quê?"
2. "Livro que você releu mais de 1 vez · qual mensagem ficou diferente na segunda leitura?"
3. "Música que ouve quando precisa pensar · o que ela ativa?"
4. "Jogo (RPG · vídeo-game · tabuleiro) que te ensinou alguma coisa de vida"
5. "Esporte que praticou · o que aprendeu fora da quadra?"
6. "Pessoa real (não famosa · alguém que você conheceu) que te mudou · o quê dela ficou?"
7. "Cena de cinema ou momento de série que você não esquece"
8. "Conceito acadêmico (mesmo nunca usado no trabalho) que te explicou o mundo"
9. "Lugar (cidade · país · casa) que te formou · o que esse lugar te ensinou?"
10. "Hobby que parece sem conexão com seu trabalho mas alimenta seu jeito de pensar"

### Regras de avanço

- **Mínimo 10 referências** (estação fala disso · skill recusa < 10)
- **Mínimo 3 com ano explícito** (formato `<Título> (<Tipo> · <Ano> · <Autor>)`)
- **Diversidade de tipo:** pelo menos 4 tipos diferentes (não pode ser 10 livros)
- **Nenhuma referência genérica:** lista negra do anti-slop §5 (sem "livros de marketing", "filmes dos anos 80")

### Regras de recusa

- Aluno entrega só livros de marketing/negócios — recusa · "as referências profissionais não te formaram · te treinaram · quero o que te FORMOU"
- Repertório com 0 datas — recusa · "preciso de ano em pelo menos 3 referências"
- Aluno copia o repertório de um exemplo ou de alguém que admira — recusa · "está pescando · me conta o SEU"

### Transição

> "Repertório registrado. [N referências · M tipos]. Próxima estação: Princípios não-negociáveis · §3."

## §5 · Estação 2B · Negócio Real + Contexto Competitivo (Brand B2B/Híbrido)

Usa as 6 dimensões do negócio (abaixo), conduzidas por pergunta.

### D1 · Negócio Real

> Como o dinheiro entra na empresa? · Descreva os canais de receita · quem paga · qual produto/serviço tem maior margem · qual maior volume.

Aprofundamento se superficial:
- "Qual canal gera mais receita hoje — digital · físico · distribuição indireta?"
- "Onde está a maior margem: produto · serviço · recorrência?"
- "O modelo depende de aquisição constante ou tem base recorrente?"

### D3 · Contexto Competitivo Real

> O que mudou na categoria ou nos concorrentes nos últimos 12-18 meses que é relevante?

- "Quem cresceu mais na categoria · por quê?"
- "Teve aquisição · fusão · entrada de player novo · saída?"
- "O que os concorrentes diretos estão fazendo em comunicação que está funcionando?"

### D4 · O Que Já Foi Tentado

> Qual foi a última iniciativa de comunicação/marketing relevante? · O que aconteceu · o que esperava vs o que ocorreu?

- "Por que parou ou não foi adiante?"
- "Causa atribuída ao resultado?"
- "Alguma ação que funcionou bem que precisa ser preservada?"

### D5 · Dados Disponíveis

> Quais dados a empresa realmente tem acesso hoje? · Analytics · CRM · pixel · histórico vendas · NPS · pesquisa?

Verificação por categoria:
- "Google Analytics configurado? GA4 com conversões rastreadas?"
- "Histórico de e-mail além do checkout? CRM com segmentação?"
- "FPD: coleta dados além de nome e email na compra?"
- "Acesso ao Meta Ads Manager com conversões?"

### D6 · O Que o Cliente Realmente Quer (objetivo não-dito)

> Esta é a mais importante e a mais ignorada. Não é o objetivo de negócio — é o que **a liderança realmente quer** com este trabalho.

- "O que muda pra QUEM CONTRATOU este trabalho se for bem-sucedido? · não pra empresa · pra a PESSOA"
- "Pressão interna pra provar valor do marketing pro board?"
- "Lançamento/evento crítico nos próximos meses que este canon precisa alimentar?"
- "Qual seria o sinal de sucesso pessoal pra quem contratou?"

### Regras de avanço

Cada dimensão (D1, D3, D4, D5, D6) precisa de pelo menos 1 dado concreto:
- D1: canal de receita + margem mencionada
- D3: 1+ movimento competitivo identificado
- D4: 1+ iniciativa passada com resultado
- D5: 3+ fontes de dado avaliadas (mesmo que "não tem")
- D6: objetivo pessoal/político do decisor identificado

### Regras de recusa

- "Não sei" sem "quem saberia?"
- Solução de comunicação como problema (D2 era pra ser tratado em D1 do briefing original mas aqui está integrado em D4)
- Tudo genérico ("queremos crescer", "mais alcance")

### Transição

> "Contexto B2B registrado. Próxima estação: Princípios não-negociáveis da marca · §3."

## §6 · Estação 3 · Princípios não-negociáveis (universal)

### Abertura canônica

> Liste 5 princípios não-negociáveis · o que você se recusa a fazer mesmo se pagassem.
>
> Cada princípio precisa de **1 frase descrevendo uma decisão real** que demonstra. Não vale "transparência" sozinho — vale "transparência radical: publico preço cheio no site · não negocio desconto · não tenho link de afiliado escondido".

### Aprofundamento

1. "Qual a última vez que você recusou trabalho · por quê?"
2. "Qual tipo de cliente você ABSOLUTAMENTE não tolera?"
3. "Que convicção forte te torna 'peculiar' ou diferente da maioria?"
4. "Em que decisão você foi contra o conselho de todos · e ganhou?"
5. "O que você ensina seus filhos/equipe que é não-negociável?"

### Modo Brand B2B

> Liste 5 princípios não-negociáveis da empresa · não os "valores" do site institucional (sustentabilidade · diversidade · etc) — os que se fossem violados causariam saída do CEO ou cisão. Cada um com 1 decisão concreta que demonstra.

### Regras de avanço (CRÍTICO · anti-Slop)

Skill valida em tempo real contra `anti-slop-rules.md` §4:
- **Princípios genéricos sem ancoragem são RECUSADOS automaticamente**
  - "Autenticidade" sozinho → recusa
  - "Transparência radical: publico preço cheio no site · não negocio" → aceita

### Regras de recusa

- 0-2 princípios — insuficiente · força mais
- 3-4 sem ancoragem em decisão — recusa cada um
- 5+ todos genéricos — recusa todos · loop volta com banco alternativo
- Princípios contradizem entre si — destacar · forçar resolução

### Transição

> "Princípios validados. Próxima estação: Decisões pré-programadas · o operacional dos princípios · §4."

## §7 · Estação 4 · Decisões pré-programadas (universal · NOVA)

### Abertura canônica

> Liste 5 "eu sempre" e 5 "eu nunca" · decisões em que você NUNCA hesita · e por quê.
>
> São decisões operacionais · não filosóficas. Concretas o suficiente pra você dizer "isso aconteceu terça passada" se eu perguntar.

### Aprofundamento (perguntas-teste pra forçar concretude)

1. "Quando recebe email de cliente sábado de tarde · você responde quando · e por quê?"
2. "Quando alguém oferece job freelance que paga bem mas é fora do território · você aceita?"
3. "Quando vê outro do seu mercado posando de guru no LinkedIn · você comenta?"
4. "Quando uma campanha sua é elogiada mas você sabe que foi sorte · você corrige?"
5. "Quando o cliente pede algo que você sabe que não vai funcionar · você obedece ou confronta?"
6. "Quando recebe DM perguntando 'quanto custa?' · você responde com preço ou pede contexto antes?"
7. "Quando precisa cobrir prazo apertado · você sacrifica qualidade · escopo ou margem?"
8. "Quando aparece oportunidade que sai do canon · você aceita pra explorar ou recusa?"

### Modo Brand B2B

> Liste 5 "a empresa sempre" e 5 "a empresa nunca" · decisões operacionais que se fossem desobedecidas causariam reprimenda interna. Não vale "sempre entregamos qualidade" — vale "sempre fazemos kickoff de 60 min antes de qualquer projeto, mesmo cliente recorrente".

### Regras de avanço

- Mínimo 5+5 (10 decisões totais)
- Cada uma com pelo menos 1 evento real que demonstra (mesmo que abstrato como "essa semana")
- 3+ decisões devem mencionar comportamento operacional específico (horário, formato, ferramenta)

### Regras de recusa

- "Sempre faço meu melhor" / "Nunca decepciono" → recusa · platitude
- Decisões contradizem princípios da Estação 3 → flag de contradição · força resolução

### Transição

> "Decisões pré-programadas registradas. Próxima estação: Voz canônica · como você FALA · §5."

## §8 · Estação 5 · Voz canônica (universal · NOVA)

### Abertura canônica

> Vamos destilar sua voz canônica em 3 camadas: **marcadores linguísticos · vocabulário hub · zona proibida**.
>
> 1. **Marcadores:** quais frases SÓ você fala? · pode ser cacoete · expressão regional · construção peculiar
> 2. **Vocabulário hub:** quais palavras você usa que outros do seu mercado não usam?
> 3. **Zona proibida:** quais cacoetes do mercado te incomodam de cara?

### Mineração reversa (se aluno trava OU se há corpus)

> Cola aqui 3 textos seus que você acha que soou autêntico · de qualquer contexto (post · email pra cliente · conversa WhatsApp salva). Vou destilar padrões linguísticos automaticamente.

Skill analisa via heurística:
- Palavras únicas (TF-IDF simples · não-comum em PT-BR)
- Construções repetidas (n-gramas frequentes)
- Tom (formal · coloquial · técnico · acadêmico)
- Marcadores de signature (ex: "Mano do céu", "Só que não", "Tamo aqui")

### Aprofundamento

1. "Qual palavra/expressão você usa que outros do seu mercado não usam?"
2. "Qual jargão do seu mercado você se recusa a usar · por quê?"
3. "Tem alguma referência cultural (filme · livro · música) que você cita sempre?"
4. "Quando você quer cortar conversa rápida · qual sua frase?"
5. "Você usa emoji em texto profissional? · Quais sim · quais nunca?"
6. "Você usa primeira pessoa singular ou plural? · em que contexto cada um?"

### Modo Brand B2B

> Mineração reversa: cola 3 peças oficiais da empresa (manifesto · email pra cliente · post de LinkedIn corporativo). Vou destilar padrões. Depois você confirma/corrige.

### Regras de avanço

- Mínimo 3 marcadores linguísticos com função explicada (não decoração)
- Mínimo 5 entradas de vocabulário hub
- Mínimo 5 itens na zona proibida (palavras ou construções)
- 1 exemplo de uso pra cada marcador

### Regras de recusa

- Marcadores genéricos tipo "olá", "bom dia", "obrigado" → recusa
- Vocabulário sem distinção do mercado → "qual a diferença entre 'estratégia' como VOCÊ usa vs como o mercado usa?"

### Transição

> "Voz registrada. Próxima estação: Inimigos & territórios · §6."

*(Estação 5B · Identidade Visual roda DEPOIS desta — método + template completos em `design-system-template.md`.)*

## §9 · Estação 6 · Inimigos & territórios (universal)

### Abertura canônica

> Vou te pedir 3 coisas:
>
> 1. **3 inimigos NOMEADOS** · pessoa real · marca real · comportamento concreto. Nada de "guru genérico". Nome + razão.
> 2. **Renegado (público)** · quem se descolou do consenso do mercado · 1 parágrafo descrevendo
> 3. **Territórios canônicos** · de 8 categorias editoriais que vou te mostrar · escolha 3-5

### Aprofundamento · inimigos

1. "Qual pessoa famosa do seu mercado você acha sobrevalorizada · por quê?"
2. "Qual marca grande você acredita que vai sumir em 5 anos · por quê?"
3. "Qual prática do seu mercado é golpe disfarçado de método?"
4. "Quem é o cliente que você NÃO quer mesmo pagando bem?"
5. "Em que sub-grupo do seu mercado você quer ser referência · não no mercado todo?"

### Aprofundamento · renegado

1. "Descreve seu cliente ideal · idade · cargo · momento de carreira · o que ele já tentou · por que parou"
2. "Qual a frase que ele fala em voz alta quando ninguém ouve?"
3. "O que ele diria se você o descrevesse como você o vê?"

### Territórios · skill apresenta as 8 categorias

> Aqui estão as 8 categorias editoriais canônicas (ver `arquetipos-de-marca.md`):
>
> 1. Estratégia & Posicionamento
> 2. Comunicação Integrada (PESO)
> 3. Growth & Performance
> 4. Experiência & Ativação
> 5. Sistemas de Marca
> 6. Dados & Inteligência (FPD/GEO)
> 7. IA & Martech
> 8. Cultura & Ciclos
>
> Escolha **3-5** · distribuídas em:
> - 1 âncora (60% do conteúdo)
> - 2 suporte (30%)
> - 1-2 piscadela (10%)
>
> **NÃO escolha tudo** — isso vira gigantismo. Se você quer 6+, está fugindo de foco.

### Regras de avanço (CRÍTICO · anti-Slop §6)

- Inimigos: 3+ com NOME PRÓPRIO (pessoa · marca específica · comportamento concreto)
- Inimigos: 0 genéricos tipo "guru sem dado" sem nome
- Renegado: 1+ parágrafo com pelo menos 3 traços concretos
- Territórios: 3-5 escolhidos · com âncora marcada
- 6+ territórios → recusa · força foco

### Transição (Creator/Híbrido → Estação 8 · Brand B2B → Estação 7)

**Creator/Híbrido:**
> "Inimigos e territórios validados. Próxima estação: Tese central · §8."

**Brand B2B:**
> "Inimigos validados. Antes da tese · vamos passar pelas Hipóteses Priorizadas · §7."

## §10 · Estação 7 · Hipóteses Priorizadas (Brand B2B)

Matriz de hipóteses priorizadas, conduzida por pergunta. **SÓ roda em modo Brand B2B** · Creator/Híbrido pula direto pra Estação 8.

### Abertura canônica

> Com base no que mapeamos das Estações 0-6 · qual sua hipótese sobre o que está acontecendo no negócio?
>
> Vou te ajudar a gerar 5-8 hipóteses no formato canônico **Se / Então / Validado por** · depois priorizamos via matriz Impacto × Verificabilidade.

### Formato obrigatório de hipótese

```
H[N] — [Nome curto]
Se [condição observável que pode ser verdadeira],
então [consequência mensurável esperada],
validado por [dado específico + ferramenta gratuita pra verificar].
```

**Exemplo canônico:**
```
H3 — Ausência de GEO
Se a empresa não tem estratégia pra motores generativos,
então quando consultamos ChatGPT sobre "<categoria>",
a marca não aparece como recomendação,
validado por teste direto em ChatGPT/Gemini/Perplexity (gratuito · 2 min).
```

### Categorias obrigatórias (cobrir todas)

- [ ] 1+ hipótese de posicionamento/comunicação
- [ ] 1+ hipótese de canal/distribuição
- [ ] 1+ hipótese de dado/mensuração
- [ ] 1+ hipótese de comportamento do consumidor
- [ ] 1+ hipótese de contexto competitivo

### Matriz de Priorização (Impacto × Verificabilidade)

| Impacto | Verificabilidade | Prioridade |
|---|---|---|
| Alto | Imediata (<30 min · ferramenta grátis) | **P1 · Validar agora** |
| Alto | Semanas (dado interno) | **P2 · Validar na semana** |
| Médio | Imediata | **P2** |
| Médio | Semanas | **P3 · Validar no mês** |
| Alto | Meses (campanha · pesquisa) | **P3** |
| Baixo | Qualquer | **P4 · Registrar não priorizar** |

### Output da Estação 7

Lista priorizada de 5-8 hipóteses · cada uma classificada P1-P4 · com plano de verificação em 3 linhas pra cada P1 e P2.

### Regras de avanço

- 5-8 hipóteses geradas (não 3 · não 10)
- Cada uma no formato Se/Então/Validado por
- Todas as 5 categorias cobertas
- Pelo menos 2 hipóteses classificadas como P1 ou P2

### Regras de recusa

- "Acredito que..." / "Parece que..." → não é hipótese · força reescrita
- Hipóteses que não podem ser refutadas → recusa
- 2 hipóteses apontando pra mesma causa com palavras diferentes → consolida

### Transição

> "Hipóteses registradas. Próxima estação: Tese central · §8."

## §11 · Estação 8 · Tese central (universal)

### Abertura canônica

> Agora vamos destilar a **Tese Central** · a hipótese estruturante que organiza tudo que você vai fazer e dizer.
>
> Se você tivesse 1 frase pra mudar o seu mercado · qual seria?
>
> Não vale "ajudar empresas a crescer" · não vale "ser referência em [setor]". Vale a frase que · se você pintasse na parede do escritório · faria sentido todo dia.

### Aprofundamento

1. "O que você acredita sobre seu mercado que 90% dos pares não acreditam?"
2. "Qual a crença comum do mercado que você desafia diariamente?"
3. "Se você publicasse manifesto de 100 palavras · qual seria a frase FINAL?"
4. "O que vai estar óbvio em 5 anos que hoje as pessoas ainda discutem?"
5. "Em que você 'pisou no aceleratorio' e foi contra o consenso · e ganhou?"

### Regras de avanço (CRÍTICO · anti-Slop §7)

Tese válida deve ter:
- **Verbo de ação** (transformar · construir · derrubar · provar · revelar · etc.)
- **Máximo 25 palavras**
- **1+ substantivo específico** do setor (não "marca", "empresa", "negócio" sozinhos)
- **1+ tensão** (oposição · pivô · ruptura)

**Exemplos canônicos válidos:**
- "Transformo branding estático em sistema de marca inteligente" (Gui Loureiro, autor das Forjas)
- "Vet bom é antropólogo · não técnico · porque pet é espelho do dono" (exemplo de uma veterinária)
- "Marca não é manual · é motor que roda sem você" (versão Forja)

**Exemplos recusados:**
- "Ajudar empresas a crescer" → sem verbo de ação · sem tensão · genérico
- "Ser a melhor consultoria de [setor] do Brasil" → meta, não tese
- "Acreditar no poder da autenticidade" → platitude · sem ancoragem

### Desdobramentos

Após tese aprovada · skill pergunta:
> "Liste 3 desdobramentos da sua tese · cada um é uma sub-tese que explica 1 aspecto. Ex: tese = 'X' · desdobramento 1 = 'isso significa que [Y1]' · desdobramento 2 = '...'"

### Regras de recusa

- Tese sem verbo → recusa
- Tese genérica (sem substantivo de setor) → recusa
- Tese > 25 palavras → recusa · força concisão
- Tese sem tensão → "qual a posição oposta? · ela existe?"

### Transição

> "Tese central registrada. Próxima estação: Frase-síntese · §9 · vamos destilar — o alvo é 7 palavras, o teto é 10."

## §12 · Estação 9 · Frase-síntese (universal · Claim)

### Abertura canônica

> Última destilação: a Frase-Síntese · sua tagline canônica · máximo **10 palavras**.
>
> Vou pedir 3 versões:
>
> 1. **Direta** · [verbo transformação] + [dor que público sente] + [resultado que você já alcançou pra si mesmo]
> 2. **Poética** · metáfora ou imagem que sintetiza o trabalho
> 3. **Contraintuitiva** · começa com "não" ou "contra" · derruba crença comum

### Exemplos (do autor das Forjas · pra inspiração · NÃO copiar)

**Direta:** "Transformo branding estático em sistema de marca inteligente"
**Poética:** "Construtor de bio-engrenagens simbióticas"
**Contraintuitiva:** "Quem tem manual de marca · não tem marca"

### Aprofundamento

Skill itera com aluno até passar nos critérios:
1. "Versão 1 atual: '<X>'. Está sem verbo de ação · adicione."
2. "Versão 2 atual: '<X>'. Tem 2 adjetivos vagos ('amazing' · 'incrível'). Reescreva."
3. "Versão 3 atual: '<X>'. Não derruba crença · só nega. Qual crença comum você está cortando?"

### Regras de avanço (CRÍTICO · anti-Slop §8)

Cada versão deve ter:
- **Máximo 10 palavras**
- **Verbo de ação**
- **0 adjetivos vagos** ("amazing", "incrível", "transformador", "único", "especial")
- **1+ substantivo específico do setor**

Versão "Direta" também deve ter: dor + verbo + resultado.
Versão "Contraintuitiva" deve ter: oposição explícita.

### Regras de recusa

- "Soluções inovadoras de [X]" → recusa · genérica
- > 10 palavras → recusa
- 2+ adjetivos vagos → recusa
- Sem verbo → recusa

### Transição

> "Frase-síntese aprovada nas 3 versões. **Você terminou as 9 estações maiêuticas.** Agora skill vai compilar seu canon em 3 arquivos canônicos · Estação 10."

## §13 · Estação 10 · Compilação do Canon (skill executa)

> ⚠️ **v2.0:** a compilação gera **7 arquivos** (Brand System completo · ver `brand-system-contract.md`), não mais 3. O texto abaixo descreve a mecânica v1 (3 arquivos) · a estrutura vale · o contrato de saída é o de 7.

### Skill não pergunta · skill compila

> **Como compilar hoje:** siga a seção "Estações 10 e 11" do `SKILL.md` (com ou sem Python). Os arquivos vão para a pasta `marca/`. O formato da entrada está em `references/exemplo-input.yaml`.

Skill executa internamente:

1. Consolida dados das Estações 0-9 em estrutura YAML (in-memory)
2. Chama `scripts/compile_canon.py` com YAML como input
3. Output: 3 arquivos no diretório de trabalho do aluno:
   - `<slug>-brand.md` (Cânone autoral)
   - `<slug>-brand-voice.md` (Voz operacional)
   - `<slug>-feedback-loops.md` (Sistema vivo)

### Apresentação ao aluno

> Compilação completa. 3 arquivos gerados:
>
> 1. `<slug>-brand.md` · seu canon autoral · marca-mãe · Nível 0
> 2. `<slug>-brand-voice.md` · voz operacional · usar em toda peça
> 3. `<slug>-feedback-loops.md` · sistema vivo · onde alimentar pós-publicação
>
> Vou agora rodar o Validador anti-Slop · Estação 11.

## §14 · Estação 11 · Validação cruzada (skill executa)

### Skill chama `scripts/validate_canon.py`

Para cada um dos arquivos gerados · skill roda `validate_canon.py` · consolida resultados. Regras completas em `anti-slop-rules.md`.

### Apresentação do relatório

```
================================
VALIDADOR ANTI-SLOP · Relatório
================================

<slug>-brand.md         · score 9.0/10 · pass
<slug>-brand-voice.md   · score 8.5/10 · pass
<slug>-feedback-loops.md · score 7.0/10 · fail (3 violações high)

Total de violações: 3
- §4 · 2 princípios genéricos sem ancoragem
- §5 · Repertório com 2 refs datadas (mínimo 3)

Força reescrita: SIM

Volta às Estações 3 e 2 pra ajustar · depois re-rodo Validador.
```

### Loop de validação

1. Se `forca_reescrita = false` em todos os arquivos → canon finalizado · entrega ao aluno
2. Se `forca_reescrita = true` em qualquer um → volta à(s) estação(ões) com violação · aluno corrige · re-roda Validador
3. Após 3 ciclos · skill oferece "aceitar com flag de risco":
   > "Validador rejeitou 3 vezes. Você pode:
   > (a) tentar uma 4ª vez com perguntas diferentes
   > (b) aceitar canon com flag de risco · loop evolutivo (V3) vai te alertar pra revisar em 30 dias"

### Entrega final

Quando validação passa:

> 🎉 **Canon de [aluno] finalizado.**
>
> **Status:** Pass · score médio [X.X]/10 · [N] violações totais (todas medium/low)
>
> **Arquivos gerados:**
> - `<slug>-brand.md` ([X] KB)
> - `<slug>-brand-voice.md` ([X] KB)
> - `<slug>-feedback-loops.md` ([X] KB)
>
> **Próximos passos:**
> 1. Os 7 arquivos já estão na sua pasta `marca/`; guarde uma cópia onde você guarda o resto (Drive, Notion, NotebookLM)
> 2. Carregar como material de referência da IA que você usa (projeto no Claude, GPT, Gem)
> 3. Usar canon como contexto de toda peça que você produzir nos próximos 6 meses
> 4. Revisar canon a cada 6 meses (ou após 50 peças publicadas)
> 5. **Próxima Forja:** `/forjas:estrategia`, que transforma esta marca num plano de 90 dias
>
> Bem-vindo à Forja.

⚠️ **A Forja NÃO termina aqui.** Após a Estação 11 · dispara AUTOMATICAMENTE a Estação 12 · Propagação Canon (não-opcional) — ver `propagacao-canon.md`.
