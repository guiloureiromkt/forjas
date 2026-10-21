# As Forjas

*[English below](#english)*

As Forjas são quatro skills do Claude Code que ajudam você a construir a sua marca conversando. Em vez de entregar um modelo pronto, elas fazem perguntas, uma de cada vez, e no fim deixam os documentos escritos na sua pasta: a alma da marca, um plano de 90 dias e a arquitetura dos canais.

Elas servem para quem tem um negócio, uma marca pessoal ou um cliente e quer sair do "posto quando dá" para um plano com motivo. Você não precisa saber marketing nem programação: basta ter o Claude Code (o aplicativo do Claude, na aba Code, ou o terminal) e tempo para responder com calma.

## As quatro Forjas, e em que ordem

| Forja | O que ela faz | Quanto tempo | Comando |
|---|---|---|---|
| **Alma** | Descobre quem a marca é: origem, princípios, voz, identidade visual, inimigos e público. Gera 7 arquivos. É a base das outras. | 3 a 5 horas, em 1 a 3 sessões | `/forjas:alma` |
| **Estratégia** | Transforma a marca num plano: diagnóstico do que está bem e do que está errado, plano de 90 dias e um manual para o time. | 30 a 60 minutos | `/forjas:estrategia` |
| **Campo de Batalha** | Decide em quais canais lutar, com que frequência e em que formato, e monta o calendário peça por peça. | 3 a 5 horas, em 2 ou 3 sessões | `/forjas:campo-de-batalha` |
| **Expressa** | Atalho para quem já tem tudo documentado (site, manual de marca, propostas): lê o material, pergunta só o que falta e entrega plano e calendário numa sessão. | 45 a 90 minutos | `/forjas:expressa` |

A ordem natural é **Alma → Estratégia → Campo de Batalha**. Se você já tem bastante material escrito sobre a marca, comece pela **Expressa**: se faltar alguma coisa, ela mesma diz qual Forja rodar antes, com o comando.

## Instalar

Dentro do Claude Code, na conversa, cole os dois comandos (um de cada vez):

```
/plugin marketplace add guiloureiromkt/forjas
/plugin install forjas@forjas
```

Depois, **feche e abra a sessão**. As Forjas só aparecem na sessão seguinte.

### Como saber que funcionou
Digite `/forjas` na conversa. A lista deve mostrar `alma`, `estrategia`, `campo-de-batalha` e `expressa`.

Se não aparecer nada, feche e abra a sessão de novo. Se ainda assim não aparecer, rode `/plugin` e confira se `forjas` está na lista de instalados.

## Os primeiros 5 minutos

1. **Abra o Claude Code na pasta da sua marca.** Se ainda não existe, crie uma pasta (por exemplo `Minha Marca`) e abra o Claude Code nela. É ali que tudo vai ficar.
2. Digite o comando da Forja, por exemplo `/forjas:alma`.
3. A Forja se apresenta, diz quanto tempo leva e quais arquivos vai criar.
4. **Na primeira vez, o Claude Code vai pedir permissão** para ler alguns arquivos de apoio que vieram com as Forjas (numa pasta dentro de `.claude/plugins`). Pode aceitar, inclusive marcando para não perguntar de novo: são só os textos das próprias Forjas. Sem essa leitura, a Forja para e avisa, em vez de inventar.
5. Comece a responder. Uma pergunta de cada vez.

## Onde fica o resultado

Tudo fica na sua pasta, e nada é enviado para lugar nenhum:

- **`marca/`** — os documentos de cada Forja (a alma da marca, o plano, o calendário).
- **o Master Brief** — um resumo vivo da marca, que todas as Forjas leem antes de perguntar e atualizam no fim. Assim, a Estratégia não pergunta de novo o que a Alma já descobriu. Por padrão ele fica em `.cycle/master-brief.md`; se já existir um, as Forjas usam o que existe.

## Parar e voltar

Pode fechar no meio. Cada Forja guarda o progresso na pasta `marca/`. Quando você chamar a mesma Forja de novo, ela diz onde vocês pararam e pergunta se continua dali.

## As Forjas e o Cycle

As Forjas funcionam sozinhas. Se você também usa o [Cycle](https://github.com/guiloureiromkt/cycle-engineering) (o método de pensamento guiado do mesmo autor), os dois dividem o mesmo Master Brief: quando o Cycle identifica que um pedido é de marketing, ele manda para a Forja certa.

## Quem mantém

Gui Loureiro. As Forjas são usadas na mentoria dele e corrigidas conforme o uso, sem prazo garantido de resposta. Encontrou um problema? Abra um aviso na aba *Issues* deste repositório no GitHub dizendo qual Forja, em que estação parou e a versão que aparece na abertura (por exemplo "Forjas v0.1.0").

Licença MIT.

---

<a id="english"></a>
## English

The Forjas ("forges") are four Claude Code skills, in Brazilian Portuguese, that help you build a brand through conversation. Instead of handing you a template, they ask questions one at a time and leave the finished documents in your folder: the brand's core, a 90-day plan and a channel architecture.

| Skill | What it does | Command |
|---|---|---|
| **Alma** | Finds out who the brand is: origin, principles, voice, visual identity, enemies and audience. The base for the others. | `/forjas:alma` |
| **Estratégia** | Turns the brand into a plan: diagnosis, 90-day plan and a team manual. | `/forjas:estrategia` |
| **Campo de Batalha** | Picks the channels, cadence and formats, and builds the content calendar. | `/forjas:campo-de-batalha` |
| **Expressa** | A shortcut for brands that already have documentation: reads it, asks only what is missing, delivers plan and calendar in one session. | `/forjas:expressa` |

**Install** (in a Claude Code conversation, then restart the session):

```
/plugin marketplace add guiloureiromkt/forjas
/plugin install forjas@forjas
```

Open Claude Code in your brand's folder and type a command. On first use, Claude Code asks for permission to read the skills' own support files inside `.claude/plugins`; allow it. Everything stays in your folder: the documents in `marca/` and a living summary, the Master Brief, shared with [Cycle](https://github.com/guiloureiromkt/cycle-engineering). You can stop and resume; progress is saved.

Maintained by Gui Loureiro on a best-effort basis. MIT license.
