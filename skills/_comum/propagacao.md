# Propagação: a Forja só termina quando o que ela descobriu chega onde é usado

## Por que existe
Uma Forja descobre coisas que mudam a marca: a voz, o público, o que se diz e o que não se diz. O erro comum é gravar os arquivos numa pasta e parar. Enquanto isso, o site, a bio, os modelos de post e as outras skills continuam usando a versão antiga, e cada peça nova sai com a marca velha sem ninguém perceber. Este protocolo fecha esse buraco.

## As três obrigações de toda Forja

### 1 · Ler o que já existe antes de perguntar
Antes da primeira pergunta, leia:
1. o Master Brief (conforme `master-brief.md`);
2. os arquivos de Forjas anteriores na pasta `marca/` e os estados `.forja-state-*.json`;
3. o que a pessoa apontar como material da marca (site, documentos, bio, propostas);
4. se a pasta aberta tem um `CLAUDE.md`, as instruções dele sobre onde a marca vive.

Depois, diga em uma frase: "li N arquivos; M coisas já decididas vou considerar". Se faltar algo importante, diga o que falta antes de seguir.

A Alma é a base: Forjas posteriores consomem e estendem o que ela decidiu sobre identidade, voz e inimigos. Nunca criam uma versão paralela.

### 2 · Gerar o arquivo de propagação
Além dos arquivos próprios, toda Forja grava `marca/<marca>-propagacao-<forja>.md`:

```markdown
# <Forja> · <marca> · propagação
Data: AAAA-MM-DD · Forjas v0.1.0

## 1. Descobertas
D1, D2, … cada uma com: o conteúdo (1-2 frases) · de onde veio (pergunta, material, inferência) · se é nova, se estende algo ou se contradiz algo (e, se contradiz, o quê e onde).

## 2. Onde cada descoberta precisa chegar
| Descoberta | <destino 1> | <destino 2> | … |
Destinos: os lugares onde a marca é usada (site, bio, modelos, apresentações, outras skills, o CLAUDE.md da pasta). Estado por célula: ✅ aplicado · 🟡 parcial · ❌ falta · ⚠️ contradiz · n/a.

## 3. Plano, por prioridade
P0 · bloqueia (sem isso, o que se produz sai errado) · P1 · importante · P2 · pode esperar · P3 · quando der. Cada item com o tempo estimado.

## 4. Pendências
- [ ] cada item ainda não aplicado
```

Se a pasta aberta tem um `CLAUDE.md` que diz onde a marca vive (um vault, uma pasta de canon, um repositório), esses são os destinos da tabela.

### 3 · Fechar
1. Mostre a tabela e o plano.
2. Pergunte: "Aplico agora o que é P0 e P1, ou deixamos anotado para depois?"
3. **Agora:** aplique P0 e P1 nos destinos que estão na pasta aberta, um de cada vez, mostrando o que mudou; P2 e P3 ficam como pendência.
4. **Depois:** o arquivo fica com as pendências marcadas, e a §6 do Master Brief ganha uma linha apontando para ele.
5. Atualize o Master Brief (§0, §6, §8 e §9) e diga qual é o próximo passo, com o comando.

## As três regras que saem disso
- **Leitura obrigatória:** toda Forja lê o que já existe (obrigação 1) e gera o arquivo de propagação (obrigação 2). Sem esse arquivo, a Forja não terminou.
- **A Alma é a base:** identidade, voz e inimigos se decidem na Alma; as outras Forjas consomem e estendem.
- **Arquivo guardado não é Forja terminada:** a Forja termina quando a propagação aconteceu ou ficou anotada como pendência, com dono.

## Base de conhecimento (opcional)
Se a pessoa tem uma base de conhecimento (cadernos do NotebookLM, uma pasta de referências, um vault), consulte-a durante a Forja, entre a etapa de explicar e a de sintetizar, e cite de onde veio cada número. Sem base, siga sem esse passo.
