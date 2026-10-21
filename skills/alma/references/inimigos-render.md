# {{ aluno.nome }} — Inimigos & Posicionamento

> Output da Estação 6 (standalone) de A Forja da Alma · sessão {{ session.data }}.

## Inimigos nomeados
{% for i in aluno.inimigos | default([]) %}
- **{{ i.nome }}** ({{ i.tipo }}) — {{ i.razao }}
{% else %}
(definir inimigos nomeados)
{% endfor %}

## Renegado (o público que se descolou do consenso)
{{ (aluno.renegado if aluno.renegado is defined else None) | default((aluno.publico.primario if aluno.publico else None) | default("(definir o renegado)")) }}

## Posicionamento competitivo
{% if aluno.posicionamento is defined and aluno.posicionamento %}
**Slot único:** {{ aluno.posicionamento.slot | default("—") }}

{% for v in aluno.posicionamento.vs | default([]) %}
- **vs {{ v.nome }}:** {{ v.diferenca }}
{% endfor %}

- **Disputa:** {{ aluno.posicionamento.disputa | default([]) | join(" · ") }}
- **NÃO disputa:** {{ aluno.posicionamento.nao_disputa | default([]) | join(" · ") }}
{% else %}
(definir posicionamento competitivo)
{% endif %}

---
**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
