#!/usr/bin/env python3
"""Check repository-local Markdown targets and SVG XML without network access."""
from pathlib import Path
import json
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
documents = sorted(ROOT.glob('README*.md')) + [ROOT / 'CONTRIBUTING.md', ROOT / 'SECURITY.md']
documents.extend(sorted((ROOT / 'docs').glob('*.md')))
documents.extend(sorted((ROOT / 'wiki').glob('*.md')))
for required in ('README.md', 'README.ru.md', 'README.de.md', 'README.es.md',
                 'wiki/Home.md', 'wiki/Home-ru.md', 'wiki/_Sidebar.md'):
    if not (ROOT / required).is_file():
        errors.append(f'Missing documentation entry point: {required}')

# These three wiki families are complete translations, not short language stubs.
# Check navigation and source references as part of the existing offline CI check.
languages = json.loads((ROOT / 'wiki' / 'languages.json').read_text(encoding="utf-8"))
codes = [language['code'] for language in languages]
if len(codes) != 24 or len(set(codes)) != 24:
    errors.append('wiki/languages.json must contain 24 distinct languages')
for family, steps, bullets in (('Connection', 4, 0), ('Home', 0, 8),
                               ('Troubleshooting', 5, 0)):
    source = (ROOT / 'wiki' / f'{family}.md').read_text(encoding="utf-8")
    references = {url for url in re.findall(r'\]\(([^\s)]+)\)', source)
                  if url.startswith('https:')}
    for language in languages:
        code = language['code']
        suffix = '' if code == 'en' else f'-{code}'
        page = ROOT / 'wiki' / f'{family}{suffix}.md'
        if not page.is_file():
            errors.append(f'Missing complete wiki translation: {page.name}')
            continue
        text = page.read_text(encoding="utf-8")
        navigation = re.search(r'<!-- language-navigation:start -->(.*?)'
                               r'<!-- language-navigation:end -->', text, re.S)
        if not navigation:
            errors.append(f'{page.name}: missing language navigation')
        else:
            for target in languages:
                target_code = target['code']
                target_suffix = '' if target_code == 'en' else f'-{target_code}'
                expected = (f'href="{family}{target_suffix}.md" '
                            f'lang="{target_code}" dir="{target.get("dir", "ltr")}"')
                if expected not in navigation.group(1):
                    errors.append(f'{page.name}: missing navigation to {target_code}')
        if language.get('dir') == 'rtl' and f'<div dir="rtl" lang="{code}">\n\n' not in text:
            errors.append(f'{page.name}: missing RTL prose container')
        if len(re.findall(r'^\d+\. ', text, re.M)) != steps:
            errors.append(f'{page.name}: expected all {steps} numbered steps')
        if len(re.findall(r'^- ', text, re.M)) < bullets:
            errors.append(f'{page.name}: expected all {bullets} reference bullets')
        targets = set(re.findall(r'\]\(([^\s)]+)\)', text))
        if not references <= targets:
            errors.append(f'{page.name}: missing source references: {sorted(references - targets)}')
for document in documents:
    text = document.read_text(encoding="utf-8")
    for target in (re.findall(r'\]\(([^\s)]+)\)', text)
                   + re.findall(r'href="([^"]+)"', text)):
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
