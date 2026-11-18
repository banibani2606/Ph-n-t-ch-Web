#!/usr/bin/env python3
"""Static schema guard; cannot replace import/integration tests."""
from pathlib import Path
import json, sys, re

def validate(path):
    w=json.loads(path.read_text(encoding='utf-8'))
    errs=[]
    for required in ('name','nodes','connections','settings'):
        if required not in w: errs.append(f'missing {required}')
    names=[n.get('name') for n in w.get('nodes',[])]
    ids=[n.get('id') for n in w.get('nodes',[])]
    if len(names)!=len(set(names)):errs.append('duplicate node names')
    if len(ids)!=len(set(ids)):errs.append('duplicate node IDs')
    for name, outputs in w.get('connections',{}).items():
        if name not in names:errs.append(f'connection source missing {name}')
        for channel in outputs.values():
            for group in channel:
                for edge in group:
                    if edge['node'] not in names: errs.append(f'missing target {edge["node"]}')
    if w.get('active') is True:errs.append('scaffold must be inactive')
    if not any(n.get('type','').endswith(('webhook','scheduleTrigger')) for n in w.get('nodes',[])):
        errs.append('no trigger')
    raw=path.read_text(encoding='utf-8')
    if re.search(r'(sk-[A-Za-z0-9]{18,}|AIza[A-Za-z0-9_-]{30,}|\d{9,}:[A-Za-z0-9_-]{25,})',raw):
        errs.append('possible embedded secret')
    if 'REPLACE_WITH_YOUR_GATEWAY_HOST' not in raw:
        print(f'INFO {path}: no placeholder detected; check actual TLS and credential setup manually')
    return errs

def main():
    files=sorted(Path(sys.argv[1] if len(sys.argv)>1 else 'generated').glob('*.json'))
    if not files: sys.exit('FAIL no JSON workflows found')
    bad=0
    for p in files:
        try: errors=validate(p)
        except Exception as exc: errors=[str(exc)]
        print(('FAIL' if errors else 'PASS')+f' {p.name}: '+('; '.join(errors) if errors else 'static structure OK'))
        bad+=bool(errors)
    print('NOTE: PASS does not mean the endpoints, credentials, Farm, Google Sheets, Telegram or Apify work.')
    sys.exit(1 if bad else 0)
if __name__=='__main__':main()
