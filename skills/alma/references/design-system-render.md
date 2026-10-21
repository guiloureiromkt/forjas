# {{ aluno.nome }} — Design System

> Output da Estação 5B (Identidade Visual) de A Forja da Alma · sessão {{ session.data }}.

## North star
{{ aluno.design.north_star | default("(definir a cor-assinatura da marca)") }}

## Tipografia
{% if aluno.design and aluno.design.tipografia %}
- **Display:** {{ aluno.design.tipografia.display | default("—") }}
- **Corpo:** {{ aluno.design.tipografia.corpo | default("—") }}
- **UI:** {{ aluno.design.tipografia.ui | default("—") }}
{% else %}
(não definido)
{% endif %}

## Paleta
{% for c in (aluno.design.paleta if aluno.design else []) | default([]) %}
- **{{ c.token }}** `{{ c.hex }}` — {{ c.papel }}
{% else %}
(definir paleta)
{% endfor %}

## Modos
{% for m in (aluno.design.modos if aluno.design else []) | default([]) %}
- **{{ m.nome }}** — {{ m.bg }} / {{ m.fg }} · accent {{ m.accent }} · onde: {{ m.onde }}
{% endfor %}

## Sub-sistemas de design
{% for s in (aluno.design.sub_sistemas if aluno.design else []) | default([]) %}
- **{{ s.nome }}** — {{ s.descricao }} ({{ s.onde }})
{% endfor %}

## Identidade fotográfica / wardrobe
{{ (aluno.design.wardrobe if aluno.design else None) | default("(não definido)") }}

## World building (consistência · ethos)
{{ (aluno.design.world_building if aluno.design else None) | default("(não definido)") }}

## Anti-padrões
{% for a in (aluno.design.anti_padroes if aluno.design else []) | default([]) %}
- ❌ {{ a }}
{% endfor %}

---
**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
