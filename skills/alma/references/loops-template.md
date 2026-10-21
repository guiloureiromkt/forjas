# {{ aluno.nome }} — Loops de aprendizagem (sistema vivo)

> Loops que vão tornar o canon de {{ aluno.nome_curto }} evolutivo · não estático.
> Gerado pela Estação 10 · A Forja da Alma · {{ session.data }}.

## Convenção · 1 loop = 1 entrada

Cada loop tem:
- **Nome** · identificador
- **Tipo** · Skill ativa · Documento canônico · Feedback consolidado · Skill a construir
- **Gatilho** · o que faz o loop rodar
- **Output** · arquivo de aprendizado alimentado
- **Consumido por** · skills/decisões que leem esse aprendizado
- **Status** · ✅ Operacional · 🟡 Em construção · 🔴 Gap (a construir)

---

## Loops iniciais sugeridos (post-Forja)

{% for item in aluno.loops_sugeridos %}
### Loop {{ item.numero }} · {{ item.nome }}

- **Tipo:** {{ item.tipo }}
- **Gatilho:** {{ item.gatilho }}
- **Output:** `{{ item.output_file }}`
- **Consumido por:** {{ item.consumido_por }}
- **Status:** 🔴 A construir · prioridade {{ item.prioridade }}
- **Alimenta canon:** {{ item.alimenta }}

{% endfor %}

## Cadência sugerida de revisão

| Frequência | O que revisar |
|---|---|
| **Semanal** | Quais marcadores linguísticos funcionaram em peças publicadas |
| **Mensal** | Quais princípios não-negociáveis foram testados · ainda valem? |
| **Trimestral** | Tese central ainda é a mesma? Audiência mudou? |
| **Semestral** | Canon completo · qual % ainda é verdade? Pivô necessário? |

## Onde alimentar feedback

- `{{ aluno.nome_curto_slug }}-feedback-voz.md` · calibração de voz pós-publicação
- `{{ aluno.nome_curto_slug }}-feedback-territorio.md` · qual território performa mais
- `{{ aluno.nome_curto_slug }}-feedback-canal.md` · qual canal converte mais

## Princípio canônico

**Canon estático morre.** Toda peça publicada é input pra evolução do canon. Pelo menos 1 ajuste por mês é sinal saudável. Zero ajustes em 6 meses = canon não tá sendo usado em produção real.

---

**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
