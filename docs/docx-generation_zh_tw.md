# docx-generation 安裝與使用說明（繁體中文）

## 1. 安裝依賴
確保已安裝 Python 3.11+，然後執行：

```bash
uv pip install python-docx pytest   # pytest 為測試用，非必須
```

## 2. 建立文件
在 `create_docx` 目錄下使用下列指令生成 .docx 文件：

```bash
python cli.py --title "我的文件" --content "這是一段範例內容。" --output "我的文件.docx"
```

## 3. 參數說明
- `--title`：文件標題，會以一級標題顯示。
- `--content`：正文文字，支援換行 (`\n`)。
- `--output`：輸出檔名（預設 `output.docx`）。

## 4. 例子
```bash
python cli.py --title "會議紀錄" \
              --content "日期: 2026-06-23\n參與者: ZEUS、HELIOS" \
              --output "會議紀錄.docx"
```

執行後會在指定路徑產生 `會議紀錄.docx`。

## 5. 測試（可選）
```bash
pytest tests/test_generate.py -v
```

## 6. 常見問題
- **中文顯示異常？** 請確保終端編碼為 UTF-8，或在 CMD/PowerShell 執行 `chcp 65001`。
- **沒有權限寫入？** 選擇可寫入的目錄，或以系統管理員身分執行。

---

這份說明已放在 `docs/` 目錄下，您也可以在 `docx-generation` skill 中查看完整英文說明。