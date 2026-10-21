# O Master Brief: onde mora e como cada Forja escreve nele

O Master Brief é o dossiê vivo da marca: um arquivo só, lido primeiro e atualizado por último por toda Forja. Ele é o mesmo arquivo que o Cycle usa (`guiloureiromkt/cycle-engineering`), com a mesma numeração de seções. Nunca existe um segundo brief.

## 1. Achar o brief (antes de qualquer pergunta)
1. Se a pasta aberta tem `.cycle/config.json` com a chave `master_brief`, o brief é o arquivo que essa chave aponta.
2. Se não tem a chave, procure arquivos chamados `master-brief.md` na pasta aberta e nas subpastas (ignore `.git` e `node_modules`).
   - **Nenhum:** o brief será `.cycle/master-brief.md`. Ele só é criado na hora de escrever (passo 3), com a §1 e a seção desta Forja. Crie só esse arquivo dentro de `.cycle/`; não crie mais nada do Cycle.
   - **Um:** use esse.
   - **Mais de um:** pergunte de qual marca é este trabalho, mostrando a lista, antes de escrever qualquer coisa. Cada marca tem o seu brief.
3. Diga à pessoa, em uma frase, qual arquivo você está usando ("vou guardar o que a gente decidir em `…/master-brief.md`").

## 2. Ler
Leia o brief inteiro antes de perguntar. O que ele já responde não se pergunta de novo: diga "isso já está no brief, vou usar" e pule.

## 3. As seções
0 onde estamos · 1 quem (e o público) · 2 a decisão ou o problema, e as decisões tomadas · 3 hipóteses · 4 material recebido · 5 achados (5.1 diagnóstico, 5.2 pesquisa de mercado, 5.3 pesquisa de público, 5.4 marca, 5.5 estratégia, 5.6 crescimento e canais, 5.7 cenários) · 6 lacunas · 7 rota recomendada e como saber · 8 histórico · 9 passagem para o próximo.

| Forja | Escreve em |
|---|---|
| Alma | §5.4 |
| Estratégia | §5.5 |
| Campo de Batalha | §5.6 |
| Expressa | §5.5 e §5.6, marcando "via Expressa" |

Toda Forja, ao terminar, também atualiza: §0 (onde estamos), §6 (o que ficou sem resposta), §8 (uma linha de histórico com a data) e §9 (para qual Forja ou passo seguir, com o comando).

## 4. Escrever sem estragar o que já existe
- **Escreva só na sua seção** e nas quatro acima. Nunca reescreva a seção de outra Forja ou de outro passo.
- **Seção que já tem conteúdo:** acrescente um bloco novo `### <Forja> · <AAAA-MM-DD>` no fim da seção. Nunca apague o anterior; se ele ficou superado, diga isso no bloco novo.
- **Brief num formato mais antigo:** aceite os rótulos que encontrar (a §7 pode se chamar "Caminho recomendado"; a §9 pode citar nomes antigos de Forja). Escreva na seção pelo número.
- **Cada achado leva o tipo e a confiança:** [Fato] com fonte e data, [Inferência] ou [Opinião]; 🟢 🟡 🔴. Um 🔴 é hipótese, nunca aposta.
- **Material confidencial** (números de cliente, documentos privados) entra como indicação de onde está, não como cópia.
