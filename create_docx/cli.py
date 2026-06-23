#!/usr/bin/env python3
"""
cli.py - Thin command‑line wrapper that calls generate.build_docx().

Usage:
    python cli.py --title "My Doc" --content "Hello world" --output out.docx
"""

import sys
from pathlib import Path

# Add the parent directory (where generate.py lives) to the import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if (PROJECT_ROOT / "generate.py").exists():
    sys.path.insert(0, str(PROJECT_ROOT))

from generate import build_docx


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate a .docx file with a title and body content."
    )
    parser.add_argument("--title", required=True, help="Document title")
    parser.add_argument(
        "--content", required=True, help="Body text (can contain newlines)"
    )
    parser.add_argument(
        "--output",
        default="output.docx",
        help="Output .docx filename (default: output.docx)",
    )
    args = parser.parse_args()

    try:
        generated_path = build_docx(
            title=args.title, content=args.content, output=args.output
        )
    except Exception as exc:  # pragma: no cover – CLI error path
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"✅ Document generated: {generated_path.resolve()}")


if __name__ == "__main__":
    main()