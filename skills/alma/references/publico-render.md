# {{ aluno.nome }} — Público (ICP)

> Output consolidado (Master Brief §5.3 + Estação de público) · A Forja da Alma · sessão {{ session.data }}.

## ICP
{{ (aluno.publico.icp if aluno.publico else None) | default((aluno.publico.primario if aluno.publico else None) | default("(definir ICP)")) }}

## O que ele já tentou (e travou)
{% for t in (aluno.publico.ja_tentou if aluno.publico else []) | default([]) %}
- {{ t }}
{% endfor %}

## Dores
{% for d in (aluno.publico.dores if aluno.publico else []) | default([]) %}
- {{ d }}
{% endfor %}

## Tensões profundas (não-ditas)
{% for t in (aluno.publico.tensoes if aluno.publico else []) | default([]) %}
- {{ t }}
{% endfor %}

## Anti-ICP (NÃO é cliente)
{% for a in (aluno.publico.anti_icp if aluno.publico else []) | default([]) %}
- {{ a }}
{% endfor %}

{% if aluno.publico and aluno.publico.secundario %}
**Público secundário:** {{ aluno.publico.secundario }}
{% endif %}
{% if aluno.publico and aluno.publico.nao_atende %}
**Não atende:** {{ aluno.publico.nao_atende }}
{% endif %}

---
**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
