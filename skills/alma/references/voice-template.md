# {{ aluno.nome }} — Voz operacional (Brand Voice)

> Documento operacional · usado por toda skill de produção (post, carrossel, newsletter, vídeo).
> Output da Estação 5 de A Forja da Alma · sessão {{ session.data }}.

## 1. Tom dominante

{{ aluno.voz.tom_dominante_long }}

**Distribuição de arquétipos** (max 100%):
{% for arq in aluno.voz.arquetipos %}
- **{{ arq.nome }}** ({{ arq.percentual }}%): {{ arq.aplicacao }}
{% endfor %}

## 2. Marcadores linguísticos canônicos

São **ferramentas de argumento** · não decoração. Cada peça publicada usa pelo menos 1.

{% for marcador in aluno.voz.marcadores %}
### "{{ marcador.frase }}"

- **Função:** {{ marcador.funcao }}
- **Quando usar:** {{ marcador.quando }}
- **Exemplo do uso:** {{ marcador.exemplo }}

{% endfor %}

## 3. Vocabulário hub (palavras canônicas)

{% for termo in aluno.voz.vocabulario_hub %}
- **{{ termo.palavra }}** → {{ termo.significado }} (não confundir com: {{ termo.nao_confundir }})
{% endfor %}

## 4. Zona proibida

### 4.1 Palavras-guru proibidas

{% for palavra in aluno.voz.zona_proibida.palavras %}
- ❌ {{ palavra }}
{% endfor %}

### 4.2 Construções proibidas

{% for construcao in aluno.voz.zona_proibida.construcoes %}
- ❌ "{{ construcao.padrao }}" — usar em vez: "{{ construcao.alternativa }}"
{% endfor %}

### 4.3 Cacoetes de IA proibidos (PT-BR · estende Will Francis)

{% for cacoete in aluno.voz.zona_proibida.cacoetes_ia %}
- ❌ {{ cacoete }}
{% endfor %}

## 5. Estrutura canônica de peça (Lei do Gancho)

- **Gancho:** primeiros 200 caracteres decidem · usa número específico OU desafia crença OU revela erro
- **Carne:** dados ancorados (empresa + número + data) · zero claim sem evidência
- **Corte (signature):** pelo menos 1 marcador linguístico de §2
- **CTA dual mundos:** "X ou Y?" (cria posicionamento) · NÃO "me conta nos comentários"

## 6. Anti-Slop · checklist obrigatório antes de publicar

- [ ] Tem dado com empresa + número + data?
- [ ] Soa como conversa real · não como newsletter?
- [ ] Tem pelo menos 1 corte/marcador (§2)?
- [ ] Livre de palavra da zona proibida (§4)?
- [ ] CTA cria dois mundos · não pede genérico?
- [ ] Primeira frase publicável como tweet isolado?
- [ ] Se guru genérico publicaria isso sem constrangimento → reescrever

## 7. Ciclo histórico como prova (não como analogia)

Quando usar referência histórica:
- ❌ ERRADO: "É como quando o Facebook mudou o algoritmo · a história se repete"
- ✅ CERTO: "Em 2012, o alcance gratuito do Facebook caiu 49% em 18 meses · marcas que dependiam exclusivamente foram destruídas · 2025 é 2012 com IA no lugar do Facebook"

Estrutura: **data + dado específico + consequência documentada + "X é Y com Z no lugar de W" + implicação prática**.

## 8. Assinatura padrão

{{ aluno.voz.assinatura_padrao }}

---

**Gerado por A Forja da Alma {{ session.versao_skill }} · {{ session.data }}**
