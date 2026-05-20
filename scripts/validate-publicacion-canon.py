#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [
    'biblioteca/README.md',
    'prompting-universal/playbook-prompting-universal-2026.html',
    'programa-empoderamiento/cartilla-programa-empoderamiento-2026.html',
    'claude-jarvis/jarvis-os-en-claude-playbook.html',
    'claude-jarvis/jarvis-os-claude-runbook.html',
    'claude-jarvis/clase-jarvis-os-en-claude-masterclass.html',
    'claude-jarvis/workbook-jarvis-os-en-claude-masterclass.html',
    'ejercicio-clase-jarvis-os-en-claude.html',
    'claude-jarvis/ejercicio-clase-jarvis-os-en-claude.html',
    'claude-jarvis/scaffolding-base/index.html',
    'claude-jarvis/scaffolding-base/01_Estaciones/Contexto Profesional/index.html',
    'cartillas-ia/cartilla-chatgpt-v3.html',
    'cartillas-ia/cartilla-gemini-v3.html',
    'cartillas-ia/cartilla-kimi-v3.html',
    'cartillas-ia/cartilla-notebooklm-v3.html',
    'cartillas-ia/cartilla-comparativa-v3.html',
    'estudio/cartilla-tecnicas-estudio-v3.html',
]

class IdParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]; self.hrefs=[]; self.modals=[]; self.titles=0
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.append(d['id'])
        if 'href' in d and d['href'].startswith('#'): self.hrefs.append(d['href'][1:])
        if 'data-modal' in d: self.modals.append(d['data-modal'])
        if 'data-modal-id' in d: self.modals.append(d['data-modal-id'])
        if tag.lower() == 'title': self.titles += 1

def fail(msg):
    print('FAIL', msg)
    sys.exit(1)

for rel in EXPECTED:
    p=ROOT/rel
    if not p.exists(): fail(f'missing {rel}')

with open(ROOT/'prompts_universales_v3000.json', encoding='utf-8') as f:
    data=json.load(f)
prompts=data.get('prompts', [])
if data.get('total') != 2026 or data.get('cap') != 2026 or len(prompts) != 2026:
    fail('prompts_universales_v3000.json contract mismatch')
ids=[p.get('id') for p in prompts]
if len(ids) != len(set(ids)):
    fail('duplicate prompt ids')
invokes=[]
for item in prompts:
    val=item.get('invoke', [])
    invokes.extend(val if isinstance(val, list) else [val])
if len(invokes) != len(set(invokes)):
    fail('duplicate invokes in v3000')

with open(ROOT/'prompts_universales_v2026_prompster.json', encoding='utf-8') as f:
    prompster=json.load(f)
if not isinstance(prompster, dict) or len(prompster) < 1000:
    fail('prompster bundle unexpectedly small')

for p in list(ROOT.glob('*.html')) + [Path(x) for x in EXPECTED if x.endswith('.html')]:
    path = p if p.is_absolute() else ROOT/p
    text=path.read_text(encoding='utf-8', errors='ignore')
    if '/Users/deonto/' in text:
        fail(f'absolute local path in {path.relative_to(ROOT)}')
    if '00_Recursos/informacion-personal' in text or 'memory/personas/personales' in text:
        fail(f'privacy path in {path.relative_to(ROOT)}')
    parser=IdParser(); parser.feed(text)
    if parser.titles == 0:
        fail(f'missing title in {path.relative_to(ROOT)}')
    dup={x for x in parser.ids if parser.ids.count(x)>1}
    if dup:
        fail(f'duplicate ids in {path.relative_to(ROOT)}: {sorted(list(dup))[:5]}')
    ids=set(parser.ids)
    broken=[h for h in parser.hrefs if h and h not in ids and not h.startswith(('http','mailto'))]
    # Allow top anchors in imported legacy-like documents with JS routing; report only severe volume.
    if len(broken) > 25:
        fail(f'too many broken local anchors in {path.relative_to(ROOT)}: {len(broken)}')

print('publicacion_canon_ok')
