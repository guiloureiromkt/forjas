# CLAUDE.md — Armadilhas conhecidas de A Forja da Alma

Documento vivo · cresce a cada sessão de aluno que revela bug ou limite.

## Seção §1 · Armadilhas iniciais (V1 launch)

### 1. Aluno trava na Estação 2 (Repertório) por bloqueio criativo

**Sintoma:** "não lembro de referências formativas"
**Workaround:** ir pra `references/perguntas-maieuticas.md` § Estação 2 banco alternativo · usar perguntas-âncora secundárias ("último filme que te marcou nos últimos 12 meses"; "livro que você releu mais de 1 vez"; "música que ouve quando precisa pensar")

### 2. Aluno copia um exemplo em vez de construir a marca dele

**Sintoma:** output da Estação 10 tem mais de 60% de texto igual a um exemplo ou a uma marca de referência
**Detecção:** `validate_canon.py` flagga via diff similarity
**Workaround:** recusar canon · perguntar "qual sua versão DISSO?" · forçar originalidade em pelo menos 7 das 10 estações

### 3. Aluno entrega princípios genéricos

**Sintoma:** Estação 3 retorna "autenticidade", "transparência", "excelência" sem ancoragem em decisão
**Detecção:** `validate_canon.py` flagga via zona proibida + regex
**Workaround:** "e isso significa O QUÊ na prática · em qual decisão de quarta-feira de manhã isso te afetou?"

### 4. Aluno B2B (V2) traz Deep Research vago

**Sintoma:** dados de imprensa/campanhas chegam genéricos · sem ancoragem
**Workaround:** forçar 3+ artigos com data · 3+ campanhas com nome · 3+ concorrentes nomeados antes de seguir pra Estação 3

### 5. Validador anti-Slop bate em loop infinito

**Sintoma:** aluno reescreve 3+ vezes · validator continua rejeitando
**Workaround:** após 3 rejeições · skill oferece "aceitar com flag de risco" + nota no canon final · loop evolutivo (V3) deve revisar

## Seção §2 · Limites conhecidos da V1

- Mineração da Estação 0.5 é 100% manual (cola + print) · automatização entra na V2
- Validador anti-Slop é heurística · não 100% preciso · falsos positivos possíveis
- Não funciona com aluno cético de IA · skill assume buy-in mínimo do método maiêutico
