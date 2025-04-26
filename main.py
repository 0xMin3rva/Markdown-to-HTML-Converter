#!/usr/bin/env python3

import argparse
import os
import markdown
import sys
import re
import json
from datetime import datetime

# Constants
DEFAULT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        pre, code {
            font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
            background-color: #f6f8fa;
            border-radius: 3px;
        }
        pre {
            padding: 16px;
            overflow: auto;
            line-height: 1.45;
        }
        code {
            padding: 0.2em 0.4em;
        }
        pre code {
            padding: 0;
        }
        blockquote {
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
            margin: 0;
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        h1 {
            padding-bottom: 0.3em;
            border-bottom: 1px solid #eaecef;
        }
        h2 {
            padding-bottom: 0.3em;
            border-bottom: 1px solid #eaecef;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }
        table {
            width: 100%;
            overflow: auto;
            border-collapse: collapse;
            margin-bottom: 16px;
        }
        table th, table td {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }
        table th {
            font-weight: 600;
        }
        table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }
        img {
            max-width: 100%;
            box-sizing: border-box;
        }
        .metadata {
            color: #6a737d;
            font-size: 0.85em;
            margin-bottom: 20px;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="metadata">
        <div>Generated on: {date}</div>
        {author_html}
    </div>
    {content}
</body>
</html>
"""

def read_markdown_file(file_path):
    """Read markdown content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def write_html_file(file_path, html_content):
    """Write HTML content to a file"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML file successfully created: {file_path}")
    except Exception as e:
        print(f"Error writing file {file_path}: {e}")
        sys.exit(1)

def extract_title(markdown_content):
    """Extract title from markdown content (first h1)"""
    # Look for the first heading
    match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
    if match:
        return match.group(1)
    return "Converted Markdown"

def convert_markdown_to_html(markdown_content, extensions=None):
    """Convert markdown content to HTML"""
    if extensions is None:
        extensions = ['extra', 'codehilite', 'toc']
    
    try:
        html = markdown.markdown(markdown_content, extensions=extensions)
        return html
    except Exception as e:
        print(f"Error converting markdown to HTML: {e}")
        sys.exit(1)

def load_template(template_path=None):
    """Load HTML template from file or use default"""
    if template_path and os.path.exists(template_path):
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading template file {template_path}: {e}")
            print("Using default template instead.")
    
    return DEFAULT_TEMPLATE

def load_metadata(metadata_path):
    """Load metadata from JSON file"""
    if metadata_path and os.path.exists(metadata_path):
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading metadata file {metadata_path}: {e}")
    
    return {}

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML")
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument("-o", "--output", help="Output HTML file (default: input file with .html extension)")
    parser.add_argument("-t", "--template", help="Custom HTML template file")
    parser.add_argument("-m", "--metadata", help="Metadata JSON file for additional information")
    parser.add_argument("-a", "--author", help="Author name to include in the HTML")
    parser.add_argument("-e", "--extensions", help="Comma-separated list of markdown extensions to use")
    parser.add_argument("--toc", action="store_true", help="Include table of contents")
    parser.add_argument("--no-style", action="store_true", help="Exclude CSS styling")
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' does not exist")
        sys.exit(1)
    
    # Determine output file
    output_file = args.output
    if not output_file:
        base_name = os.path.splitext(args.input)[0]
        output_file = f"{base_name}.html"
    
    # Read markdown content
    markdown_content = read_markdown_file(args.input)
    
    # Extract title from markdown content
    title = extract_title(markdown_content)
    
    # Prepare markdown extensions
    extensions = []
    if args.extensions:
        extensions = [ext.strip() for ext in args.extensions.split(',')]
    else:
        extensions = ['extra', 'codehilite']
    
    if args.toc:
        extensions.append('toc')
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(markdown_content, extensions)
    
    # Load metadata
    metadata = load_metadata(args.metadata)
    
    # Use command-line author if provided, otherwise use from metadata
    author = args.author or metadata.get('author', '')
    author_html = f'<div>Author: {author}</div>' if author else ''
    
    # Load template
    template = load_template(args.template)
    
    # Remove styling if requested
    if args.no_style:
        template = re.sub(r'<style>.*?</style>', '', template, flags=re.DOTALL)
    
    # Format template with content
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    final_html = template.format(
        title=title,
        content=html_content,
        date=current_date,
        author_html=author_html
    )
    
    # Write HTML file
    write_html_file(output_file, final_html)

if __name__ == "__main__":
    main()
