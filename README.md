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
git clone https://github.com/0xMin3rva/markdown-to-html.git
cd markdown-to-html
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

## 📝 Examples

### Basic conversion:
```bash
python main.py README.md
```

### Specify output file:
```bash
python main.py README.md -o docs/index.html
```

### Include author information:
```bash
python main.py README.md -a "Your Name"
```

### Use a custom HTML template:
```bash
python main.py README.md -t templates/custom.html
```

### Include table of contents:
```bash
python main.py README.md --toc
```

### Use specific markdown extensions:
```bash
python main.py README.md -e tables,fenced_code,footnotes
```

### Convert without styling:
```bash
python main.py README.md --no-style
```

### Use metadata from a JSON file:
```bash
python main.py README.md -m metadata.json
```

## 📊 Example Output

The tool generates clean HTML output with a responsive, GitHub-like style by default:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Documentation</title>
    <style>
        /* CSS styling omitted for brevity */
    </style>
</head>
<body>
    <div class="metadata">
        <div>Generated on: 2023-09-12 15:30:45</div>
        <div>Author: Your Name</div>
    </div>
    <h1>Project Documentation</h1>
    <p>This is a sample markdown document converted to HTML.</p>
    <h2>Features</h2>
    <ul>
        <li>Feature 1</li>
        <li>Feature 2</li>
        <li>Feature 3</li>
    </ul>
    <!-- More converted HTML content... -->
</body>
</html>
```

## 🎨 Customization

### Custom HTML Templates

You can create your own HTML template by creating a file with placeholders:

- `{title}`: The title extracted from the markdown
- `{content}`: The converted HTML content
- `{date}`: The generation date and time
- `{author_html}`: HTML for the author information

Example custom template:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>{title}</h1>
        <p>By: {author_html}</p>
    </header>
    <main>
        {content}
    </main>
    <footer>
        Generated on {date}
    </footer>
</body>
</html>
```

## Metadata JSON

You can provide additional metadata using a JSON file:
```bash
{
    "author": "Your Name",
    "description": "A description of the document",
    "keywords": ["markdown", "html", "converter"]
}
```
