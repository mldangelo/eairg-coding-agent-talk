#!/usr/bin/env python3
"""
Convert talk.md content to HTML format for the website.
This script parses the markdown and extracts content for each section.
"""

import re
import json
from pathlib import Path

def parse_slidev_markdown(content):
    """Parse Slidev markdown and extract sections."""

    # Remove the frontmatter
    content = re.sub(r'^---.*?---\n', '', content, flags=re.DOTALL)

    # Split by slide separators
    slides = re.split(r'\n---\n', content)

    sections = {}
    current_act = None

    for slide in slides:
        slide = slide.strip()
        if not slide:
            continue

        # Extract title from first heading
        title_match = re.search(r'^# (.+)', slide, re.MULTILINE)
        if not title_match:
            continue

        title = title_match.group(1).strip()

        # Determine section ID
        section_id = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('&', '').replace('(', '').replace(')', '')
        section_id = re.sub(r'[^\w-]', '', section_id)

        # Track acts
        if title.startswith('Act '):
            current_act = section_id

        # Clean up content
        # Remove layout directives
        content_clean = re.sub(r'^layout:.*$', '', slide, flags=re.MULTILINE)
        content_clean = re.sub(r'^class:.*$', '', content_clean, flags=re.MULTILINE)

        # Remove comments
        content_clean = re.sub(r'<!--.*?-->', '', content_clean, flags=re.DOTALL)

        # Clean up HTML-like tags for Vue components
        content_clean = re.sub(r'<[^>]+>', '', content_clean)

        # Remove empty lines
        content_clean = '\n'.join(line for line in content_clean.split('\n') if line.strip())

        sections[section_id] = {
            'title': title,
            'content': content_clean,
            'act': current_act
        }

    return sections

def markdown_to_html(text):
    """Convert basic markdown to HTML."""

    # Headers
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Bold and italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)

    # Code blocks
    text = re.sub(r'```(\w+)?\n(.*?)\n```', r'<div class="code-block">\2</div>', text, flags=re.DOTALL)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    # Lists
    lines = text.split('\n')
    in_list = False
    result_lines = []

    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('• '):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            item = line.strip()[2:].strip()
            result_lines.append(f'<li>{item}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            if line.strip():
                result_lines.append(f'<p>{line}</p>')
            else:
                result_lines.append('')

    if in_list:
        result_lines.append('</ul>')

    return '\n'.join(result_lines)

def generate_section_html(section_id, section_data):
    """Generate HTML for a section."""

    content_html = markdown_to_html(section_data['content'])

    return f'''
            <section class="section" id="{section_id}">
                {content_html}
            </section>
'''

def main():
    # Read the markdown file
    with open('talk.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse sections
    sections = parse_slidev_markdown(content)

    # Generate HTML for each section
    sections_html = {}
    for section_id, section_data in sections.items():
        sections_html[section_id] = generate_section_html(section_id, section_data)

    # Save the extracted content as JSON for inspection
    with open('extracted_content.json', 'w', encoding='utf-8') as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(sections)} sections")
    print("Key sections found:")
    for section_id, section_data in list(sections.items())[:10]:
        print(f"  - {section_id}: {section_data['title']}")

    return sections_html

if __name__ == '__main__':
    main()