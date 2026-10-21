"""Compila o Brand System do aluno via Jinja2 · gera 7 outputs canônicos (v2.0).

Usage:
    python scripts/run.py compile_canon.py <input.yaml> <output_dir>

Inputs:
    YAML com chaves `aluno.*` e `session.*` (ver test_compile_canon.py)

Outputs (no output_dir · Brand System completo · 7 arquivos):
    <slug>-brand.md · <slug>-voice.md · <slug>-design-system.md
    <slug>-inimigos.md · <slug>-publico.md · <slug>-feedback-loops.md
    <slug>-propagacao-alma.md
"""
import argparse
import sys
from pathlib import Path

import yaml
from jinja2 import ChainableUndefined, Environment, FileSystemLoader

SKILL_DIR = Path(__file__).parent.parent
REFERENCES_DIR = SKILL_DIR / "references"

TEMPLATES = {
    "brand": "brand-template.md",
    "voice": "voice-template.md",
    "design-system": "design-system-render.md",
    "inimigos": "inimigos-render.md",
    "publico": "publico-render.md",
    "feedback-loops": "loops-template.md",
    "propagacao-alma": "propagation-render.md",
}


def compile_canon(input_yaml: Path, output_dir: Path) -> dict:
    """Compila canon · retorna dict com paths gerados."""
    with input_yaml.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    env = Environment(
        loader=FileSystemLoader(str(REFERENCES_DIR)),
        trim_blocks=True,
        lstrip_blocks=True,
        # campo que faltar no YAML vira vazio e cai no default() do modelo,
        # em vez de derrubar a compilação inteira
        undefined=ChainableUndefined,
    )

    slug = data["aluno"]["nome_curto_slug"]
    generated = {}

    for output_name, template_name in TEMPLATES.items():
        template = env.get_template(template_name)
        rendered = template.render(**data)

        output_path = output_dir / f"{slug}-{output_name}.md"
        output_path.write_text(rendered, encoding="utf-8")
        generated[output_name] = output_path

    return generated


def main():
    parser = argparse.ArgumentParser(description="Compila canon do aluno via Jinja2")
    parser.add_argument("input_yaml", type=Path, help="Path pra YAML de input")
    parser.add_argument("output_dir", type=Path, help="Diretório de output")
    args = parser.parse_args()

    if not args.input_yaml.exists():
        print(f"ERROR: input não encontrado: {args.input_yaml}", file=sys.stderr)
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated = compile_canon(args.input_yaml, args.output_dir)

    print(f"✓ Canon compilado pra: {args.output_dir}")
    for name, path in generated.items():
        print(f"  - {name}: {path}")


if __name__ == "__main__":
    main()
