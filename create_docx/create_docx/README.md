# python-docx Document Generation Workflow

This directory contains a self-contained workflow to generate Word (.docx) documents using the `python-docx` library, without requiring any Google Workspace OAuth setup.

## Directory Layout

```
create_docx/
├─ generate.py      # Core logic that builds the .docx file
├─ cli.py           # Command-line wrapper (exposes `hermes docx generate`)
├─ tests/
│   └─ test_generate.py   # Unit tests
└─ README.md        # This file
```

## Prerequisites

- Python 3.11+ (confirmed with `python --version`)
- `python-docx` library (installed via `uv pip install python-docx`)
- Optional: `pytest` for running unit tests (`uv pip install pytest`)

## Installation (if not already present)

```bash
# Ensure you're in the workspace root or any directory with access to the files
uv pip install python-docx pytest
```

## Usage

Run the CLI directly:

```bash
python cli.py --title "My Document Title" \
              --content "This is the body content.\nIt can span multiple lines." \
              --output "my_output.docx"
```

- `--title` – Required. The document title (added as Heading 1).
- `--content` – Required. Body text (plain text or with `\n` for newlines).
- `--output` – Optional. Destination filename; defaults to `output.docx`.

Example output:

```
✅ Document generated: D:\workspace\Hermes-UAMS\WorkshopV2\workspace\create_docx\my_output.docx
```

The generated `.docx` file will contain:
- The supplied title rendered as a Heading 1.
- The supplied content rendered as a normal paragraph.
- Default font size of 12 pt applied to all text.

## Running the Tests

```bash
pytest tests/test_generate.py -v
```

The test suite verifies:
- Successful document creation with expected title/content.
- That empty titles or empty content raise `ValueError`.
- The resulting `.docx` file can be read back and its text matches expectations.

## Common Issues & Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `Style 'HEADING1' not found` | Using an older version of `python-docx` that lacks built‑in styles | Upgrade the library: `uv pip install --upgrade python-docx`. |
| `File not found` when invoking `cli.py` | Running the script from a different working directory | Execute from the `create_docx` folder or use an absolute path for `--output`. |
| Unicode characters appear garbled | The terminal encoding is not UTF‑8 | Ensure your console uses UTF‑8 (e.g., Windows PowerShell/Terminal → Settings → “Use Unicode UTF‑8”). |
| PermissionError on writing output file | Output path is read‑only or occupied | Choose a writable folder (e.g., your user's `Documents` directory) or close any program locking the file. |

## Extending the Workflow

- **Styling** – Add custom fonts, sizes, or paragraph formatting by expanding `_add_heading` and `_add_content`.
- **Placeholders** – Implement simple token replacement (e.g., `{{date}}`) before saving the document.
- **Multiple Sections** – Append additional headings or tables by calling `Document.add_heading` or `Document.add_table` in `generate.py`.

## License

This workflow is provided under the MIT License. Feel free to copy, modify, and distribute it as needed.