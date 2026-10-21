# Retomar de onde parou

As Forjas são conversas longas (a Alma leva de 1 a 3 sessões). Ninguém deve perder uma resposta porque fechou a janela.

## Gravar
- O estado de cada Forja fica em `marca/.forja-state-<forja>.json` (`<forja>` = `alma`, `estrategia`, `campo-de-batalha` ou `expressa`).
- Siga o esquema de `${CLAUDE_PLUGIN_ROOT}/skills/estrategia/references/state-json-schema.md`, acrescentando no topo: `"forja"`, `"marca"` (o nome da marca), `"versao_pacote"` e `"etapa_atual"` (estação ou modo em que a conversa está).
- Grave depois de **cada** resposta aceita, não só no fim.

## Retomar
Ao abrir, antes de se apresentar de novo, procure o estado desta Forja na pasta `marca/` da marca em uso.
- **Achou, e a marca bate com a do brief:** "Da última vez paramos em <etapa> (<data>). Continuo daí, ou prefere recomeçar?" Recomeçar não apaga: guarde o estado antigo com a data no nome.
- **Achou, e a marca não bate:** pergunte se este trabalho é da marca do estado ou de outra, antes de qualquer coisa.
- **Não achou:** comece do início.
