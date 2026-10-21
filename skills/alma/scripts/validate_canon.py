"""Auditor leve · checa contradições + genericidade + zona proibida + anti-slop visual.

Usage:
    python scripts/run.py validate_canon.py <path/to/canon.md>   # 1 arquivo
    python scripts/run.py validate_canon.py <dir/>               # Brand System inteiro (7 arquivos)

Saída (stdout · YAML):
    1 arquivo → status · violacoes · score_geral · forca_reescrita
    pasta     → status agregado · total · reprovados · arquivos{nome: resultado}
"""
import argparse
import re
import sys
from pathlib import Path

import yaml


# §1 · Zona proibida palavras-guru PT-BR
ZONA_PROIBIDA_GURU = [
    "revolucionári", "game-changer", "elevar para o próximo nível", "delve",
    "divisor de águas", "mindset", "hackear", "fórmula mágica",
    "disruptiv", "conteúdo é rei", "storytelling autêntico",
    "sinergia",
]

# §2 · Vocabulário IA PT-BR (Will Francis)
ZONA_PROIBIDA_IA = [
    "aprofundar", "navega o", "sublinhar", "fomentar", "cultivar",
    "aprimorar", "robust", "multifacetad",
    "consolida-se como", "posiciona-se como", "tapeçaria",
]

# §3 · Construções proibidas (regex)
CONSTRUCOES_PROIBIDAS = [
    (r"(?i)não é (um[a]? )?\w+,? é (um[a]? )?\w+", "Construção 'Não é X, é Y'"),
    (r"(?i)sem \w+\. sem \w+\.", "Construção 'Sem X. Sem Y.'"),
    (r"(?i)e isso muda tudo", "Clichê 'e isso muda tudo'"),
    (r"(?i)no fim das contas", "Filler 'no fim das contas'"),
    (r"(?i)cada vez mais", "Filler 'cada vez mais'"),
    (r"(?i)em um mundo onde", "Abertura clichê 'em um mundo onde'"),
]

# §4 · Princípios genéricos sem ancoragem
PRINCIPIOS_GENERICOS = [
    "autenticidade", "transparência", "excelência", "qualidade",
    "ética", "respeito", "integridade", "comprometimento", "paixão",
    "inovação",
]

# §D · Anti-slop visual (só roda em arquivo de design-system)
DESIGN_SLOP_FRASES = [
    "transmite confiança", "passa confiança", "cor da confiança",
    "representa natureza", "transmite tranquilidade", "psicologia das cores",
    "cor que acalma", "cor da paixão", "remete a sensação",
]


def _strip_secoes_proibida(text: str) -> str:
    """Remove seções que DOCUMENTAM termos banidos (## Zona proibida etc.) e linhas
    com ❌ — pra não contar documentação de ban como uso real do termo."""
    linhas = []
    pulando = False
    for line in text.split("\n"):
        if re.match(r"^#{1,6}\s", line):  # novo heading reseta o estado
            low = line.lower()
            pulando = "proibid" in low or "banid" in low or "zona proibida" in low
        if pulando or "❌" in line:
            continue
        linhas.append(line)
    return "\n".join(linhas)


def _match_zona_proibida(text: str, lista: list, regra: str) -> list:
    found = []
    for palavra in lista:
        if palavra.lower() in text.lower():
            found.append({
                "regra": regra,
                "severity": "high",
                "detalhe": f"Palavra/raiz proibida encontrada: '{palavra}'",
                "sugestao": "Substituir por termo concreto do setor do aluno · ver anti-slop-rules.md",
            })
    return found


def _match_construcoes_proibidas(text: str) -> list:
    found = []
    for pattern, descricao in CONSTRUCOES_PROIBIDAS:
        if re.search(pattern, text):
            found.append({
                "regra": "§3",
                "severity": "medium",
                "detalhe": descricao,
                "sugestao": "Reescrever sem o cacoete · ver anti-slop-rules.md §3",
            })
    return found


def _check_principios_genericos(text: str) -> list:
    """Procura seção §3 Princípios · se for só lista de palavras genéricas · falha."""
    found = []
    # Heurística: pega bloco entre "## 3" e próximo "## "
    match = re.search(r"##\s*3\..*?(?=\n##\s|\Z)", text, re.DOTALL)
    if not match:
        return found
    bloco = match.group(0).lower()

    # Conta quantos princípios genéricos aparecem SEM linha de descrição após
    for principio in PRINCIPIOS_GENERICOS:
        if principio in bloco:
            # Procura se vem com descrição (linha tem mais de 30 chars após principio)
            for line in bloco.split("\n"):
                if principio in line and len(line.strip()) < 50:
                    found.append({
                        "regra": "§4",
                        "severity": "high",
                        "detalhe": f"Princípio genérico sem ancoragem: '{principio}'",
                        "sugestao": "Adicione 1 frase descrevendo decisão concreta que demonstra",
                    })
                    break
    return found


def _check_repertorio_vago(text: str) -> list:
    """Estação 2 (Repertório) precisa 3+ refs com ano (19xx ou 20xx)."""
    found = []
    match = re.search(r"##\s*6?\.?\s*Repertório.*?(?=\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE)
    if not match:
        return found
    bloco = match.group(0)

    anos = re.findall(r"\b(19|20)\d{2}\b", bloco)
    if len(anos) < 3:
        found.append({
            "regra": "§5",
            "severity": "high",
            "detalhe": f"Repertório com apenas {len(anos)} referências datadas (mínimo 3)",
            "sugestao": "Cada referência deve ter título + autor/criador + ano",
        })

    listas_negras = ["livros de", "filmes de", "música em geral", "vários livros"]
    for negra in listas_negras:
        if negra in bloco.lower():
            found.append({
                "regra": "§5",
                "severity": "high",
                "detalhe": f"Repertório vago: '{negra}'",
                "sugestao": "Nomear título específico · não categoria genérica",
            })
    return found


def _check_design_slop(text: str) -> list:
    """Anti-slop visual · só roda se o arquivo for de design-system."""
    found = []
    low = text.lower()
    if "design system" not in low and "## paleta" not in low:
        return found
    # Paleta sem nenhum hex = cor vaga
    if "## paleta" in low and not re.search(r"#[0-9a-fA-F]{3,6}\b", text):
        found.append({
            "regra": "§D1",
            "severity": "high",
            "detalhe": "Paleta sem código hex · cor vaga",
            "sugestao": "Cada cor leva hex + razão concreta da marca",
        })
    # Clichês de psicologia das cores
    for frase in DESIGN_SLOP_FRASES:
        if frase in low:
            found.append({
                "regra": "§D2",
                "severity": "medium",
                "detalhe": f"Clichê de psicologia das cores: '{frase}'",
                "sugestao": "Ancorar a cor na razão real da marca · não em psicologia genérica",
            })
    return found


def validate(canon_text: str) -> dict:
    """Valida canon · retorna dict com violacoes + score + forca_reescrita."""
    violacoes = []

    texto_sem_bans = _strip_secoes_proibida(canon_text)
    violacoes.extend(_match_zona_proibida(texto_sem_bans, ZONA_PROIBIDA_GURU, "§1"))
    violacoes.extend(_match_zona_proibida(texto_sem_bans, ZONA_PROIBIDA_IA, "§2"))
    violacoes.extend(_match_construcoes_proibidas(texto_sem_bans))
    violacoes.extend(_check_principios_genericos(canon_text))
    violacoes.extend(_check_repertorio_vago(canon_text))
    violacoes.extend(_check_design_slop(canon_text))

    high_severity_count = sum(1 for v in violacoes if v["severity"] == "high")
    medium_severity_count = sum(1 for v in violacoes if v["severity"] == "medium")

    score = max(0, 10 - (high_severity_count * 2) - (medium_severity_count * 0.5))

    return {
        "status": "pass" if score >= 8 and high_severity_count == 0 else "fail",
        "violacoes": violacoes,
        "score_geral": round(score, 1),
        "forca_reescrita": score < 8 or high_severity_count > 0,
    }


def validate_dir(directory, slug=None) -> dict:
    """Valida todos os <slug>-*.md (ou *.md) de uma pasta · agrega o Brand System."""
    pattern = f"{slug}-*.md" if slug else "*.md"
    arquivos = {}
    for f in sorted(Path(directory).glob(pattern)):
        if f.name.startswith("_"):  # ignora _INDEX.md / MOCs
            continue
        arquivos[f.name] = validate(f.read_text(encoding="utf-8"))
    reprovados = [n for n, r in arquivos.items() if r["status"] != "pass"]
    return {
        "status": "pass" if arquivos and not reprovados else "fail",
        "total": len(arquivos),
        "reprovados": reprovados,
        "arquivos": arquivos,
    }


def main():
    parser = argparse.ArgumentParser(description="Auditor leve de canon (1 arquivo ou Brand System inteiro)")
    parser.add_argument("canon_path", type=Path, help="Path pro .md OU pasta com os 7 arquivos")
    args = parser.parse_args()

    if not args.canon_path.exists():
        print(f"ERROR: não encontrado: {args.canon_path}", file=sys.stderr)
        sys.exit(1)

    if args.canon_path.is_dir():
        result = validate_dir(args.canon_path)
    else:
        result = validate(args.canon_path.read_text(encoding="utf-8"))

    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    sys.exit(0 if result["status"] == "pass" else 2)


if __name__ == "__main__":
    main()
