# Templates dos 3 Documentos · Modo Entrega

> **Princípio canon V1.1:** outputs DIDÁTICOS · cada item segue padrão **O QUE · POR QUE · O QUE FAZER**. Não pode ser lista seca de bullets.
>
> **Hard rule:** outputs personalizados · NÃO genéricos. Cada artefato cita empresa por nome · referencia respostas das 12 perguntas · ancora em estatísticas da material de referência.

---

## Documento 1 · `forja-plano-<slug>-<disciplina>-<data>.md`

**Tamanho-alvo:** 2.500-4.000 palavras
**Audiência:** o próprio usuário + 1 nível acima (diretoria/board) + agência se houver
**Tom:** executivo · cada decisão justificada · cada marco com porquê

```markdown
# Plano Estratégico · [DISCIPLINA] · [EMPRESA]
**Data:** [YYYY-MM-DD] · **Período:** Q[N]/[YYYY] (90 dias)
**Forjado com:** A Forja da Estratégia v1.3
**Pareado com:** `forja-diagnostico-<slug>-...md` · `forja-educacao-<slug>-...md`

---

## 1. Tese estratégica do trimestre

> [1 parágrafo · 4-6 linhas · sintetiza a aposta central da empresa nos próximos 90 dias]

**Por que essa tese e não outra:**
- [Característica específica da empresa que justifica · referenciando pergunta N da entrevista]
- [Ideia da material de referência que ressoa · referenciando seção do material]
- [Anti-tese que descartamos e por quê]

---

## 2. Os 3 movimentos prioritários HOJE

Cada um leva 30 minutos ou menos. Sem bloqueio. Pra fazer ainda hoje.

### Movimento 1 · [Nome curto]
**O que fazer:** [ação concreta · 1-2 frases]
**Por que esse é o primeiro:** [explicação · por que esse antecede os outros]
**Como medir que funcionou:** [sinal observável em 7 dias]

### Movimento 2 · [Nome curto]
[mesma estrutura]

### Movimento 3 · [Nome curto]
[mesma estrutura]

---

## 3. Marcos de 90 dias

Pra cada marco · explicação de porquê esse marco específico e o que muda quando acontece.

### Marco D+15 · [Nome]
**O que será entregue:** [artefato concreto · não abstração]
**Quem é responsável:** [pessoa nomeada da empresa do usuário · da pergunta 11]
**Como medir:** [métrica específica · valor antes · meta]
**Por que esse marco antecede os próximos:** [explicação encadeada]

### Marco D+30 · [Nome]
[mesma estrutura]

### Marco D+45 · [Nome]
[mesma estrutura]

### Marco D+60 · [Nome]
[mesma estrutura]

### Marco D+75 · [Nome]
[mesma estrutura]

### Marco D+90 · [Nome · revisão trimestral · Q[N+1] plan]
[mesma estrutura]

⚠️ **Regra:** cada marco precisa ser concretizável. Não aceitar marco abstrato tipo "alinhar time". Sempre artefato + responsável + métrica.

---

## 4. KPIs canon (3-5 max · sem cosmético)

Priorização — ordem importa.

### KPI 1 · [Nome]
**O que mede:** [descrição em 1 frase]
**Baseline atual:** [valor de hoje · da pergunta 5 da entrevista]
**Meta D+90:** [valor]
**Como vamos medir:** [ferramenta · fonte de dado]
**Por que esse KPI e não outro:** [explicação ancorada na material de referência]

### KPI 2-5 · [mesma estrutura]

---

## 5. KPIs que NÃO vamos perseguir (rejeitados explicitamente)

Importante listar pra alinhar expectativa com board/CFO:

- **[KPI cosmético 1]** · Por que NÃO: [razão ancorada · ex: "captura só 20-30% da jornada B2B real"]
- **[KPI cosmético 2]** · Por que NÃO: [...]

---

## 6. Sequência de execução · semana a semana

### Semana 1-2 · [Tema da fase · ex: Diagnóstico instrumentado]
**Objetivo da fase:** [1 frase]
**Ações:**
- [...]
**Output da fase:** [artefato esperado]

### Semana 3-4 · [Tema]
[mesma estrutura]

### Semana 5-6 · [Tema]
[mesma estrutura]

### Semana 7-9 · [Tema]
[mesma estrutura]

### Semana 10-12 · [Tema · validação + plano próximo trimestre]
[mesma estrutura]

---

## 7. Stack mínima viável

| Componente | Status atual (pergunta 4) | Status necessário | O que fazer |
|---|---|---|---|
| [...] | [muito uso · médio · abandonado] | [necessário] | [comprar · implementar · descontinuar] |

**Custo estimado total:** R$ [valor] em 90 dias
**ROI esperado D+90:** [%] (ancorado em estimativa da material de referência)

---

## 8. Riscos · 3 cenários que podem dar errado

### Risco 1 · [Nome]
**O que pode dar errado:** [descrição]
**Probabilidade:** [alta · média · baixa]
**Impacto se acontecer:** [descrição quantificada]
**Como mitigar:** [ação preventiva]

### Risco 2-3 · [mesma estrutura]

---

## 9. Assinatura

> Forjado com [A Forja da Estratégia](https://github.com/guiloureiromkt/forjas) · Gui Loureiro.

**Próxima revisão sugerida:** [D+90 · data exata]
```

---

## Documento 2 · `forja-diagnostico-<slug>-<disciplina>-<data>.md`

**Tamanho-alvo:** 2.500-4.000 palavras
**Audiência:** o próprio usuário · uso interno · NÃO pra board (esse é diagnóstico cru · não polido)
**Tom:** brutal honesto + DIDÁTICO · cada problema explica POR QUE é problema

```markdown
# Diagnóstico Estratégico · [DISCIPLINA] · [EMPRESA]
**Data:** [YYYY-MM-DD]
**Forjado com:** A Forja da Estratégia v1.3
**Pareado com:** `forja-plano-...md` · `forja-educacao-...md`

---

## 1. Diagnóstico em 1 frase

> [1 frase brutal e honesta · 12-20 palavras · sem suavização]

---

## 2. O que vocês fazem BEM (3-5 itens)

Pra cada item · estrutura **O QUE · POR QUE · COMO PROTEGER**:

### Ponto Forte 1 · [Nome]
**O que está acontecendo:** [descrição concreta · referenciando pergunta da entrevista]
**Por que isso é importante:** [conexão com estado-da-arte da disciplina · referenciando material de referência]
**Como proteger isso:** [movimento pra não perder esse ponto forte nos próximos 12 meses]

### Pontos Fortes 2-5 · [mesma estrutura]

---

## 3. O que tá ERRADO ou OBSOLETO (2-4 itens)

Pra cada item · estrutura **O QUE · POR QUE É GRAVE · O QUE FAZER**:

### Problema 1 · [Nome do anti-padrão]
**O que está acontecendo:** [descrição concreta com referência à pergunta da entrevista]
**Por que isso é grave:** [explicação consequencial · com estatística da material de referência · com custo estimado em R$ ou %]
**O que fazer (3 passos):**
1. **HOJE (≤30 min):** [ação imediata]
2. **Próximas 4 semanas:** [ação estrutural]
3. **Em 60 dias:** [ação de validação]

### Problemas 2-4 · [mesma estrutura]

---

## 4. GAPS · estado atual vs estado-da-arte (3-5 itens)

Cada gap mostra: onde a empresa está · onde o estado-da-arte está · quanto custa o gap · quanto tempo pra fechar.

### Gap 1 · [Nome]
**Estado atual da empresa:** [descrição · da pergunta da entrevista]
**Estado-da-arte da disciplina:** [descrição · da material de referência]
**Custo do gap (estimado):** [R$ ou % perda · com explicação]
**Tempo pra fechar (estimado):** [semanas · com pré-requisitos]
**Como começar a fechar:** [movimento de entrada · não tudo de uma vez]

### Gaps 2-5 · [mesma estrutura]

---

## 5. OPORTUNIDADES que vocês ainda não viram (2-3 itens)

Movimentos que a empresa pode fazer e que ainda ninguém na categoria fez:

### Oportunidade 1 · [Nome]
**O que é:** [descrição]
**Por que vocês têm vantagem:** [específico à empresa]
**Por que isso é momento agora:** [janela temporal · ancorada em tendência da material de referência]
**Como capturar:** [movimento de entrada com baixo custo]

### Oportunidades 2-3 · [mesma estrutura]

---

## 6. Tensão estrutural interna (da pergunta 7)

**Sua tensão (declarada):** [descrição]
**Tensão correspondente na disciplina:** [referenciando contradição interna da material de referência]
**A disciplina resolveu essa tensão?** [Sim/Não/Parcial]
**Movimento sugerido pra esta empresa:** [solução adaptada · com porquê]

---

## 7. Concorrência · análise comparativa

Da pergunta 8 (concorrentes nomeados):

| Concorrente | O que você admira | Como a material de referência enxerga | O que você pode fazer melhor |
|---|---|---|---|
| [nome] | [...] | [framework aplicável + case correlato] | [movimento defensivo/ofensivo] |

---

## 8. Tentativas falhas · análise com a material de referência

Da pergunta 9 (tentativas que não funcionaram):

| O que tentou | Por que você acha que falhou | Por que a material de referência diz que falhou | Lição transferível |
|---|---|---|---|
| [...] | [...] | [anti-padrão ou framework] | [...] |

---

## 9. Hipótese estratégica · validação

Da pergunta 10 (aposta de R$ 100k):

**Hipótese declarada:** [...]
**Ideia da material de referência que VALIDA:** [referência específica]
**Ideia da material de referência que CONTRADIZ ou MODULA:** [referência · razão]
**Veredito da Forja:** [Apoiar · Modular · Refutar com alternativa]
**Explicação do veredito:** [por que esse veredito específico]

---

## 10. Scorecard final · 10 dimensões

Score 1-10 em cada · ver rubrica em `assets/estagio-maturidade-scoring.md`

| Dimensão | Score | Por que esse score (1 linha) |
|---|---|---|
| Clareza de tese estratégica | [N]/10 | [...] |
| Alinhamento ICP declarado vs real | [N]/10 | [...] |
| Maturidade da stack | [N]/10 | [...] |
| Métricas alinhadas com estado-da-arte | [N]/10 | [...] |
| Briefing canon (não-deriva) | [N]/10 | [...] |
| Resolução de tensões internas | [N]/10 | [...] |
| Posicionamento competitivo claro | [N]/10 | [...] |
| Capacidade de aprendizado pós-falha | [N]/10 | [...] |
| Hipótese estratégica defendível | [N]/10 | [...] |
| Time + função subvalorizada reconhecida | [N]/10 | [...] |

**Score total:** [N]/100

---

## 11. Estágio de Maturidade da Marca

**Seu estágio atual:** [🔴/🟠/🟡/🟢 Frágil/Confusa/Madura/Sólida]

**O que isso significa na prática:**
[Parágrafo didático · 4-6 linhas · explicando o que esse estágio significa pra ESTA empresa especificamente]

**Por que isso é importante:**
[Parágrafo · consequência prática de estar nesse estágio · com estatística do material de referência quando aplicável]

**O que fazer pra subir pro próximo estágio:**
[Parágrafo · resumo do plano pareado · prazo estimado]

**Próximo estágio alcançável:** [estágio] · em [N] meses se executar o plano pareado.

---

## 12. Assinatura

> Forjado com [A Forja da Estratégia](https://github.com/guiloureiromkt/forjas) · Gui Loureiro.
```

---

## Documento 3 · `forja-educacao-<slug>-<disciplina>-<data>.md`

**Tamanho-alvo:** 3.000-5.000 palavras
**Audiência:** time da empresa do usuário (pleno · júnior · novos contratados)
**Tom:** professor sênior · didático · cada conceito explica POR QUE importa e ONDE NÃO usar

```markdown
# Manual Educativo · [DISCIPLINA] aplicada em [EMPRESA]
**Data:** [YYYY-MM-DD]
**Pra quem:** time interno · pleno · júnior · novos contratados
**Tempo de leitura:** 30-45 min
**Forjado com:** A Forja da Estratégia v1.3

---

## 1. Por que esse manual existe

[3-5 frases · contextualiza por que o líder tá entregando esse manual pro time. Cita o gap real da pergunta 11 · função subvalorizada · necessidade de transferibilidade]

---

## 2. O essencial da disciplina · 5 conceitos canon

Pra cada conceito (escolher 5 mais aplicáveis à empresa) · estrutura **DEFINIÇÃO · POR QUE · ONDE APLICAR · ONDE NÃO**:

### Conceito 1 · [Nome simples · sem jargão se possível]

**O que é (definição em linguagem de gente · 2-3 frases):**
[Definição limpa · sem terminologia desnecessária · se tiver termo técnico explicar inline]

**Por que isso importa pra [EMPRESA] especificamente:**
[2-3 frases · ancorado em resposta da entrevista]

**Como aplicar HOJE em [EMPRESA]:**
[1 movimento concreto · não genérico]

**Onde NÃO aplicar (contra-indicações):**
[Situações onde esse conceito vira armadilha · pra time não confundir]

**Onde aprender mais:** [link/referência da material de referência]

### Conceitos 2-5 · [mesma estrutura]

---

## 3. Frameworks aplicáveis · pra time usar

Pra cada framework (3-5 max) · estrutura **QUANDO USAR · QUANDO NÃO · COMO APLICAR**:

### Framework 1 · [Nome · autor · ano]

**Visão geral (3-4 linhas):** [...]

**Quando usar:** [situação típica]
**Quando NÃO usar:** [contra-indicações]
**Aplicação em [EMPRESA]:** [exemplo concreto baseado em respostas das perguntas]
**Erro mais comum:** [como time costuma errar isso · pra evitar]

### Frameworks 2-5 · [mesma estrutura]

---

## 4. Anti-padrões · o que NÃO fazer (3-5 itens)

Pra cada anti-padrão · explicação acessível pro time · com consequência real:

### Anti-padrão 1 · [Nome]
**O que é:** [descrição]
**Por que time confunde isso com algo bom:** [explicação · expectativa errada]
**O que acontece quando time cai nisso:** [consequência prática]
**Sinal pra parar antes de cair nisso:** [red flag observável]

### Anti-padrões 2-5 · [mesma estrutura]

---

## 5. Cases de referência (3-5 cases)

Priorizar BR · cada um com estrutura **O QUE ACONTECEU · O QUE APRENDER · COMO APLICAR**:

### Case 1 · [Empresa · ano]
**O que aconteceu:** [história em 3-5 frases]
**O que aprender:** [tese transferível]
**Como aplicar (não copiar) em [EMPRESA]:** [adaptação prática]

### Cases 2-5 · [mesma estrutura]

---

## 6. Vocabulário · 8-12 termos

Pra time conseguir falar com clareza em reunião com diretoria/agência:

| Termo | O que é (1 frase simples) | Como usar em reunião | Pra evitar |
|---|---|---|---|
| [...] | [...] | [exemplo de fala] | [confusão comum] |

---

## 7. Checklist de autodiagnóstico

Pra cada membro do time autodiagnosticar antes de tomar decisão:

- [ ] [Pergunta canon 1 · ex: "Esse briefing tem métrica + prazo + segmento ou é vácuo?"]
- [ ] [Pergunta canon 2]
- [ ] [...]

Se responder 'não' em alguma · parar e consultar líder.

---

## 8. Leituras priorizadas (próximos 30 dias)

3-5 itens · ordem priorizada (cf §10 Recomendação de Leitura da material de referência):

1. **[Item]** · Por quê · [...]
2. **[Item]** · [...]
3. [...]

---

## 9. Assinatura

> Forjado com [A Forja da Estratégia](https://github.com/guiloureiromkt/forjas) · Gui Loureiro.

**Próxima revisão sugerida:** [D+90]
```

---

## Hard rules de qualidade · aplicáveis aos 3 documentos

1. **Citar empresa por nome** sempre · NUNCA "vocês" genérico
2. **Citar pergunta específica** quando referenciar resposta do usuário ("cf pergunta 4 · stack")
3. **Citar seção do material de referência** quando referenciar fonte ("cf seção 5 · frameworks do material")
4. **Estatísticas em **bold** com fonte** sempre
5. **Padrão O QUE · POR QUE · O QUE FAZER** em cada item · em todos os 3 documentos
6. **Sem listicle "X dicas pra Y"** · canon anti-guru bloqueia
7. **Sem promessa de transformação rápida** · anti-guru
8. **PT-BR** default · markdown limpo
9. **Termos técnicos explicados na 1ª aparição** (last-click · MMM · GEO · Dark Social · PESO · zero-party data · ICP)
10. **Assinatura canon** em todos os 3 (vincula skill ↔ produto)
11. **Próxima revisão sugerida** em pelo menos plano e diagnóstico (lifecycle de cliente)
12. **Slug consistente** nos 3 arquivos (mesma empresa · mesma data · mesma disciplina)


---

# Templates de sessão (movidos do SKILL.md · 2026-07-13)

## Passo 3 · Resumo executivo pré-aprovação (V1.1)

Antes de gerar os 3 documentos · mostrar este resumo e aguardar OK do usuário:

```
═══════════════════════════════════════════
RESUMO EXECUTIVO · A Forja da Estratégia
═══════════════════════════════════════════
Empresa: <nome>
Disciplina: <nome>
Estágio de Maturidade da Marca atual: <score/estágio>
Próxima estágio alcançável: <estágio · em N meses>

Tese estratégica do trimestre (1 frase):
"<frase única>"

3 movimentos HOJE (ações de 30 min cada):
1. <ação>
2. <ação>
3. <ação>

3 marcos críticos próximos 90 dias:
- D+15: <marco>
- D+45: <marco>
- D+90: <marco>

3 anti-padrões a corrigir:
- <anti-padrão> (custo estimado: <impacto>)
- <anti-padrão> (custo estimado: <impacto>)
- <anti-padrão> (custo estimado: <impacto>)

Vou gerar 3 documentos:
- forja-plano-<slug>-<disciplina>-<data>.md
- forja-diagnostico-<slug>-<disciplina>-<data>.md
- forja-educacao-<slug>-<disciplina>-<data>.md

Aprova essa direção ou quer ajustar antes de eu salvar?
═══════════════════════════════════════════
```

## Passo 5 · Closure & Bridge (EXPANDIDO V1.5)

Após salvar os 4 arquivos canon, encerrar a sessão com 6 elementos canônicos:

**1. Confirmação concreta dos arquivos salvos** (= path canon · tamanho aprox · status):
```
Path canon: <path>
| Arquivo | Tamanho aprox. | Status |
| forja-plano.md | ~N palavras | ✅ salvo |
| forja-diagnostico.md | ~N palavras | ✅ salvo |
| forja-educacao.md | ~N palavras | ✅ salvo |
| marca/forja-estado-estrategia.json | estado completo | ✅ salvo |
```

**2. Resumo executivo da entrega** (= "o grande movimento desta Forja" em 1 parágrafo + lista de 5-10 descobertas canon HOJE + cicatrizes strategist novas)

**3. Próximos passos imediatos** (= 3 movimentos HOJE D+0-7 reforçados · auto-executáveis):
- Movimento 1: <ação específica · tempo · responsável>
- Movimento 2: <ação específica · tempo · responsável>
- Movimento 3: <ação específica · tempo · responsável>

**4. Bridge pra próxima Forja sugerida** (= 1 parágrafo curto):
- Qual disciplina rodar a seguir? (default: próxima Cat na ordem canon · ex: Estratégia → Comunicação → Growth → IA & MarTech → Sistemas de Marca → Experiência → Dados → Cultura)
- Quando? (default D+30 a D+45 · respeita ciclo de execução do plano atual)
- O que muda? (= dados zero-party coletados · spine documental publicado · etc. · alimentam Forja seguinte)

**5. Pendência meta-canon** (= se a sessão descobriu cicatriz nova strategist · documentar atualização pendente da skill):
- Skill version pendente · linha de mudança · cross-ref changelog (`references/changelog.md`)

**6. Pergunta de transição** (= "Voltamos pro que ficou pendente da sessão atual antes da Forja · ou quer encerrar por aqui?"):
- Reconhece que Forja foi inserção temporária num fluxo maior · facilita retomada

**Por que essa estrutura importa:** sem Closure & Bridge canon · sessão termina com "salvei os arquivos · até a próxima" e o usuário fica perdido sobre o que fazer AGORA. Closure & Bridge transforma a Forja em ponto-de-virada · não em entrega passiva.
