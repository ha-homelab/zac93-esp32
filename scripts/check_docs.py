#!/usr/bin/env python3
"""Check repository-local Markdown targets and SVG XML without network access."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
documents = [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md', ROOT / 'SECURITY.md']
documents.extend(sorted((ROOT / 'docs').glob('*.md')))
for document in documents:
    text = document.read_text()
    for target in re.findall(r'\]\(([^\s)]+)\)', text):
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith('#'):
            continue
        path = (document.parent / unquote(parsed.path)).resolve()
        if not path.is_relative_to(ROOT) or not path.exists():
            errors.append(f'{document.relative_to(ROOT)}: missing local target {target}')
for diagram in (ROOT / 'assets' / 'diagrams').glob('*.svg'):
    try:
        ET.parse(diagram)
    except ET.ParseError as exc:
        errors.append(f'{diagram.name}: {exc}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: local links in {len(documents)} documents; SVG XML parses.')
