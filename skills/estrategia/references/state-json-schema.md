# Schema do `forja-estado-<forja>.json`

> **Ler QUANDO:** for iniciar o Passo 1 (Modo Entrevista) e precisar criar/atualizar o state.json — ou no Modo 0.6 pra saber quais campos reutilizar. Salvar incrementalmente após CADA resposta da entrevista (não só no fim).

```json
{
  "session_id": "<uuid>",
  "started_at": "<ISO 8601>",
  "updated_at": "<ISO 8601>",
  "disciplina": "Comunicação Integrada",
  "material_referencia_source": "embarcado · assets/indice-estrategico-comunicacao-integrada.md",
  "empresa": {
    "nome": "...",
    "setor": "...",
    "porte": "...",
    "icp_declarado": "...",
    "icp_real": "...",
    "jornada_declarada": "...",
    "stack_atual": {},
    "metrica_demite": "...",
    "metrica_bonifica": "...",
    "briefing_recorrente": "...",
    "tensao_estrutural": "...",
    "concorrentes_nomeados": [],
    "tentativas_falhas": [],
    "hipotese_estrategica": "...",
    "time_estrutura": {},
    "time_funcao_subvalorizada": "...",
    "interlocutores_principais": [
      {
        "nome_ou_funcao": "...",
        "idade_aprox": "...",
        "perfil": "técnico|político|cético|entusiasta|misto",
        "referencia_intelectual": "..."
      }
    ],
    "movimento_30_dias": "..."
  },
  "alma_canon_anexa": null,
  "named_entities_ledger": {
    "pessoas_dentro_empresa": {
      "Nome A": {"funcao": "...", "contexto": "...", "tag": "INTERNO"}
    },
    "pessoas_externas": {
      "Nome X": {"relacao": "...", "contexto": "...", "tag": "EXTERNO|CLIENTE|FORNECEDOR|CONCORRENTE"}
    },
    "concorrentes": [],
    "clientes_atuais": [],
    "fornecedores": []
  },
  "pesquisa_externa": {
    "fontes_consultadas": [],
    "achados_que_contradizem_usuario": [],
    "achados_que_validam_usuario": [],
    "data_pesquisa": "<ISO 8601>"
  },
  "dado_ancorado": true,
  "perguntas_concluidas": [1, 2, 3],
  "perguntas_pendentes": [4, 5, 6]
}
```

**Notas de uso:**
- `named_entities_ledger` — obrigatório (Hard Rule #3): tag `INTERNO/EXTERNO/CLIENTE/CONCORRENTE` antes de qualquer análise sobre a entidade. Exemplo realista de calibragem em `hard-rules-precisao.md §Hard Rule #3`.
- `pesquisa_externa` — preenchido no Modo 1.5 (Hard Rule #5).
- `interlocutores_principais[]` — capturado na Pergunta 11.5 (ver `12-estacoes-entrevista.md`).
- `dado_ancorado: false` — marcar se o usuário resistir 2× a dar dado concreto (limita o diagnóstico depois).
- **Cross-Forja (Hard Rule #10):** na 2ª+ Forja da mesma empresa, campos recarregados do state anterior recebem sufixo `_REUTILIZADO_forja_anterior`.
