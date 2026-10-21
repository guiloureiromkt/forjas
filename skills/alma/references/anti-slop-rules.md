# Anti-Slop Rules · Validador de Canon

Regras de recusa aplicadas pelo `validate_canon.py` na Estação 11. Se canon falha em qualquer regra · força reescrita.

## §1 · Zona proibida · palavras-guru (PT-BR)

Match exato (case-insensitive) na §1-§9 do canon do aluno · recusa automática:

```
revolucionário · game-changer · elevar para o próximo nível · delve
divisor de águas · mindset · hackear · fórmula mágica · escalar (crescer rápido)
disruptivo · inovação (sem dado) · conteúdo é rei · storytelling autêntico
engajar (como resultado) · sinergia · jornada (sem contexto)
```

## §2 · Zona proibida · vocabulário IA PT-BR (Will Francis)

```
aprofundar · navegar (figurativo) · sublinhar · fomentar · cultivar
aprimorar · robusto · multifacetado · orgânico (figurativo)
consolida-se como · posiciona-se como · tapeçaria · ecossistema (abstrato vago)
```

## §3 · Construções proibidas

Regex match · recusa automática:

| Padrão | Razão |
|---|---|
| `(?i)não é (um[a]? )?\w+,? é (um[a]? )?\w+` | "Não é X, é Y" — cacoete IA |
| `(?i)sem \w+\. sem \w+\.` | "Sem X. Sem Y." — cacoete |
| `(?i)menos \w+\. mais \w+\.` | "Menos X. Mais Y." — cacoete |
| `(?i)e isso muda tudo` | clichê |
| `(?i)no fim das contas` | filler |
| `(?i)ao final do dia` | filler · tradução de "at the end of the day" |
| `(?i)a pergunta fica:` | cacoete IA |
| `(?i)cada vez mais` | filler vago |
| `(?i)em um mundo onde` | abertura clichê |
| `(?i)vivemos em uma era` | abertura clichê |

## §4 · Detector de princípios genéricos (Estação 3)

Se §3 do canon contém apenas palavras das listas abaixo · sem ancoragem em decisão concreta · recusa:

**Princípios proibidos sem ancoragem:**
- "autenticidade"
- "transparência"
- "excelência"
- "qualidade"
- "ética"
- "respeito"
- "integridade"
- "comprometimento"
- "paixão"
- "inovação"

**Como passar:** cada princípio DEVE vir com 1+ frase que descreve **decisão concreta** que demonstra o princípio. Ex:
- ❌ Recusado: "Transparência"
- ✅ Aceito: "Transparência radical: publico o preço cheio no site · não negocio desconto · não tenho 'link de afiliado' escondido"

## §5 · Detector de repertório vago (Estação 2)

Estação 2 (Repertório) DEVE conter pelo menos:
- 3 referências culturais específicas com **título completo + autor/criador + ano**
- 0 referências genéricas tipo "livros de marketing" · "filmes dos anos 80"

**Detecção:**
- Regex pra ano: `\b(19|20)\d{2}\b` deve aparecer em pelo menos 3 referências
- Lista negra: "livros de", "filmes de", "música em geral", "vários livros"

## §6 · Detector de inimigo genérico (Estação 6)

Estação 6 (Inimigos) DEVE nomear pelo menos:
- 1 pessoa real específica (nome próprio · não "guru genérico")
- 1 marca/empresa específica
- 1 comportamento concreto (não "marketing ruim")

**Recusa se:** todos os 3 inimigos são tipos genéricos sem nome próprio.

## §7 · Detector de tese vazia (Estação 8)

Tese central DEVE:
- Ter verbo de ação (transformar · construir · derrubar · provar · etc.)
- Ter no máximo 25 palavras
- Conter pelo menos 1 substantivo específico do setor do aluno (não "marca", "empresa", "negócio" sozinhos)

**Recusa se:** tese é abstrata pura · tipo "ajudar empresas a crescer" · sem ancoragem específica.

## §8 · Detector de frase-síntese fraca (Estação 9)

Frase-síntese DEVE:
- Ter no máximo 10 palavras
- Conter verbo de ação
- NÃO ter 2+ adjetivos vagos ("amazing", "incrível", "transformador", "único", "especial")

## §9 · Detector de cópia de exemplo

Se a marca do aluno tem 60%+ de texto igual a um exemplo deste pacote (ou a outra marca que ele trouxe como referência) · recusa com mensagem:
> "Isso está muito parecido com o exemplo. A Forja existe pra você construir a SUA marca, não pra copiar outra. Volte à Estação 2 (Repertório) e me conta as referências que SÃO suas."

## §10 · Detector de contradição interna

Cross-check entre estações:
- §3 (princípios) NÃO pode contradizer §4 (decisões pré-programadas)
  - Ex: princípio "transparência radical" + decisão pré-programada "nunca revelo metodologia" = contradição
- §6 (inimigos) NÃO pode incluir alguém que §7 (tese) defende
- §1.audiência primária NÃO pode estar em §1.público que NÃO atendemos

**Detecção:** LLM-based · análise semântica · não regex.

---

## Saída do Validador

```yaml
status: pass | fail
violacoes:
  - regra: §3
    severity: high
    detalhe: "Princípio 'integridade' sem ancoragem em decisão concreta"
    sugestao: "Adicione 1 frase descrevendo decisão que demonstra integridade"
score_geral: 7.5  # 0-10
forca_reescrita: true | false  # true se score < 8 OU 1+ violação severity:high
```

## Severidade

- **high** · força reescrita (canon não pode ser publicado)
- **medium** · aviso · canon pode ser publicado mas aluno deve revisar
- **low** · sugestão · informativo

## Loop de validação

1. Aluno completa Estações 0-9
2. Skill compila via `compile_canon.py` (Estação 10)
3. Skill valida via `validate_canon.py` (Estação 11)
4. Se `forca_reescrita = true` → loop volta à estação da violação · aluno reescreve · re-valida
5. Após 3 ciclos de recusa · skill oferece "aceitar com flag de risco" · loop evolutivo (V3) revisará
