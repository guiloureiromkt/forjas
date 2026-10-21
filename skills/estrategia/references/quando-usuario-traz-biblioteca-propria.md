# Quando o usuário traz material de referência próprio (Índice Estratégico)

> **Ler QUANDO:** a disciplina escolhida NÃO for Comunicação Integrada (material embarcado) — ou o usuário colar/compartilhar um Índice Estratégico de NotebookLM próprio (Growth · IA · Sistemas de Marca · etc.).

---

## Formato mínimo esperado (9 seções)

Aceitar um Índice Estratégico de qualquer NotebookLM desde que tenha minimamente:

1. Tese central (1 parágrafo)
2. Ideias complementares (4-8 com fonte)
3. Mapa de pessoas · marcas · conceitos · datas · estatísticas
4. Cronograma da evolução da disciplina
5. Frameworks aplicáveis
6. Tensões internas (contradições não-resolvidas)
7. Gaps de cobertura (perguntas que o material não responde)
8. Citações âncora (8-12 com fonte)
9. O que esse material rejeita (anti-padrões)

**Se faltar mais de 3 dessas 9 seções** · avisar o usuário e oferecer um prompt pra gerar o Índice no NotebookLM antes de prosseguir.

## Prompt sugerido pro usuário gerar o Índice no NotebookLM

Oferecer algo neste formato (adaptar disciplina):

```
A partir de todas as fontes deste notebook sobre [DISCIPLINA], gere um
"Índice Estratégico" com exatamente estas 9 seções:
1. Tese central (1 parágrafo)
2. 4-8 ideias complementares (cada uma com a fonte)
3. Mapa de pessoas, marcas, conceitos, datas e estatísticas citadas
4. Cronograma da evolução da disciplina
5. Frameworks aplicáveis (nome + quando usar)
6. Tensões internas (contradições não-resolvidas entre as fontes)
7. Gaps de cobertura (perguntas que o material não responde)
8. 8-12 citações âncora (literais, com fonte)
9. O que esse material rejeita (anti-padrões da disciplina)
```

## Notas operacionais

- Antes de pedir Índice novo, perguntar se a pessoa já tem uma base de conhecimento da disciplina (cf Modo 1.5 step 0).
- Registrar no state.json: `material_referencia_source: "usuário · colado em <data>"`.
- Lembrar linguagem user-facing: chamar de "material de referência" / "Índice Estratégico" — nunca "corpus" (cf `linguagem-e-tom.md`).
