# Estação 5B · Identidade Visual — template + método

> A parte "difícil" do Brand System. Extrai a identidade visual de quem NÃO é designer, via 3 fontes, em registro mentor. Output decomponível pras skills lerem.

## Como extrair (3 fontes)
1. **Web** — marca tem site/Instagram? → minera cores, fontes, estilo. Reusa `clone-webapp` (engenharia reversa visual de URL/screenshots).
2. **Prints + imagens** — a pessoa manda screenshots de posts, logo, fotos que curte → destila paleta + tipografia + mood. Reusa `image-pipeline`.
3. **Do zero** — não tem nada → maiêutica visual + sugestão ancorada. Reusa `uiux-genesis` (database de estilos/paletas/fontes) + `taste`.

## Maiêutica visual (mentor · faz pensar · zero jargão)
- "Se a tua marca fosse uma pessoa entrando numa sala, como ela tá vestida?"
- "Que 3 marcas — de qualquer setor — te dão inveja de bonito? Por quê cada uma?"
- "Que cor você JAMAIS usaria? Por quê?"
- "Tua marca é mais 'sussurro elegante' ou 'grito na cara'?"
- "Mostra uma foto/print de algo (não precisa ser de marca) que tem a 'vibe' que você quer."

## Template de saída · `<marca>-design-system.md`
```markdown
---
type: design-system
marca: "<marca>"
date: <data>
confianca: 🟡   # 🟢 extraído de marca madura · 🟡 destilado · 🔴 proposto do zero (validar)
---

# Design System · <marca>

## Paleta
| Cor | Hex | Papel | Significado/razão |
|---|---|---|---|
| Primária | #... | fundo/base | ... |
| Accent (assinatura) | #... | destaque | ... |
| Categóricas | #... | seções/ênfase | ... |
> Regra: accent é assinatura (pontual, alto contraste) · não fundo inteiro.

## Tipografia
- **Display:** <fonte> (pesos · uso)
- **Corpo:** <fonte> (uso)
- **Fallback:** <fonte websafe>

## Logo / marca
- Descrição · variações (completa · símbolo · mono) · o que NUNCA fazer

## Tokens
- Spacing · radius · sombras · transições

## Componentes canônicos
- Botões · cards · pills · etc. (descrição + quando usar)

## World building (consistência)
- **Touchpoints:** onde a marca aparece (do post à embalagem)
- **Trademarks:** assinaturas visuais/temáticas que diferenciam
- **Ethos:** a emoção que TODO ponto de contato reforça
- **Os 4 pilares que não podem falhar:** Produto · História · Experiência · Consistência

## Anti-padrões (o que NÃO fazer)
- ...
```

## Regras anti-slop visual
- ❌ paleta genérica ("azul = confiança") · ✅ cor ancorada em razão real
- ❌ fonte default (Inter/Roboto "porque sim") · ✅ escolha com porquê
- 🔴 confiança baixa = marcar como hipótese · não apresentar como verdade fechada
- Cada decisão visual conversa com a **voz** (Estação 5) e a **tese** (Estação 8) — não é decoração solta.
