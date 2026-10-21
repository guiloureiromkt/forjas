# {{ aluno.nome }} — Canon autoral (Marca Mãe · Nível 0)

> Construído via A Forja da Alma · sessão de {{ session.data }} · {{ session.duracao_total_min }} min

**Última atualização:** {{ session.data }}
**Versão:** 1.0 · canon inicial (loop evolutivo pendente · V3)
**Persona:** {{ aluno.persona }} ({{ aluno.persona_descricao }})
**Frase-síntese:** {{ aluno.frase_sintese }}

---

## 1. O que é {{ aluno.nome_curto }}

{{ aluno.identidade_paragrafo }}

**Tagline canônica:** {{ aluno.tagline }}

**Audiência primária:** {{ aluno.audiencia_primaria }}

**Inimigos nomeados:**
{% for inimigo in aluno.inimigos %}
- **{{ inimigo.nome }}** ({{ inimigo.tipo }}): {{ inimigo.razao }}
{% endfor %}

## 2. Voz canônica + marcadores linguísticos

### 2.1 Tom dominante

{{ aluno.voz.tom_dominante }}

### 2.2 Marcadores linguísticos (uso obrigatório · pelo menos 1 por peça)

{% for marcador in aluno.voz.marcadores %}
- **"{{ marcador.frase }}"** — {{ marcador.funcao }}
{% endfor %}

### 2.3 Zona proibida (palavras/construções que {{ aluno.nome_curto }} NUNCA usa)

{% for proibido in aluno.voz.zona_proibida %}
- ❌ {{ proibido }}
{% endfor %}

### 2.4 Vocabulário hub (palavras canônicas)

{% for termo in aluno.voz.vocabulario_hub %}
- **{{ termo.palavra }}** — {{ termo.significado }}
{% endfor %}

## 3. Princípios não-negociáveis · territórios · público-alvo

### 3.1 Princípios não-negociáveis (5)

{% for principio in aluno.principios %}
{{ loop.index }}. **{{ principio.titulo }}** — {{ principio.descricao }}
{% endfor %}

### 3.2 Territórios canônicos (3-5 categorias editoriais)

{% for territorio in aluno.territorios %}
- **{{ territorio.nome }}** ({{ territorio.frequencia_relativa }}%): {{ territorio.descricao }}
{% endfor %}

### 3.3 Público-alvo detalhado

**Público primário:** {{ aluno.publico.primario }}
**Público secundário:** {{ aluno.publico.secundario }}
**Público que NÃO atendemos:** {{ aluno.publico.nao_atende }}

## 4. Capacidades-marca (4 dimensões)

{% for capacidade in aluno.capacidades %}
### 4.{{ loop.index }} {{ capacidade.titulo }}

- **POV ({{ capacidade.titulo }}):** {{ capacidade.pov }}
- **Skill operacional:** {{ capacidade.skill }}
- **Produtizável como:** {{ capacidade.produtizavel }}

{% endfor %}

## 5. Decisões pré-programadas

### 5.1 SEMPRE fazer

{% for decisao in aluno.decisoes.sempre %}
- {{ decisao }}
{% endfor %}

### 5.2 NUNCA fazer

{% for decisao in aluno.decisoes.nunca %}
- {{ decisao }}
{% endfor %}

## 6. Repertório vivido (referências culturais formativas)

{% for ref in aluno.repertorio %}
- **{{ ref.titulo }}** ({{ ref.tipo }} · {{ ref.ano }}{% if ref.autor %} · {{ ref.autor }}{% endif %}) — {{ ref.por_que_te_formou }}
{% endfor %}

## 7. Tese central

> {{ aluno.tese_central }}

**Desdobramentos:**
{% for desdobramento in aluno.tese_desdobramentos %}
- {{ desdobramento }}
{% endfor %}

## 8. Loop de aprendizagem (sistema vivo)

Ver `{{ aluno.nome_curto_slug }}-feedback-loops.md` (documento irmão).

## 9. Convenção de manutenção

- Revisar canon a cada 6 meses (ou após 50 peças publicadas · o que vier primeiro)
- Atualizar §4 capacidades quando emergir nova
- Editar §3.1 princípios com extrema cautela (mudanças aqui afetam TUDO)
- §7 tese central só muda em pivô estratégico explícito (documentar em ADR)

## 10. Glossário rápido

{% for termo in aluno.glossario %}
| {{ termo.termo }} | {{ termo.significado }} |
{% endfor %}

---

**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
**Validador anti-Slop:** {{ session.validador_status }}
