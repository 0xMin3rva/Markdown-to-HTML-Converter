# 📝 Markdown to HTML Converter

A powerful command-line tool that converts Markdown files to beautifully styled HTML documents with customization options.

## ✨ Features

- 🔄 Convert Markdown files to clean, well-formatted HTML
- 🎨 Beautiful default styling that resembles GitHub's markdown style
- 📊 Support for tables, code blocks, and other extended markdown features
- 📑 Optionally generate a table of contents from headings
- 🧩 Customize output with your own HTML templates
- 📋 Include metadata like author name and generation date
- 🔧 Configure markdown extensions for advanced features
- 🔍 Extract the title automatically from the first heading

## 📋 Requirements

- Python 3.6 or higher
- markdown library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xMin3rva/Markdown-to-HTML-Converter.git
cd markdown-to-html-converter
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py <input_file.md> [options]
```

## ⚙️ Options

- `-o, --output FILE`: Output HTML file (default: input file with .html extension)
- `-t, --template FILE`: Custom HTML template file
- `-m, --metadata FILE`: Metadata JSON file for additional information
- `-a, --author NAME`: Author name to include in the HTML
- `-e, --extensions LIST`: Comma-separated list of markdown extensions to use
- `--toc`: Include table of contents
- `--no-style`: Exclude CSS styling
