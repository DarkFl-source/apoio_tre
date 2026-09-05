"""Atualiza a entrada do GitHub Pages a partir do HTML fonte revisado."""
from pathlib import Path
import argparse

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
source = (root / 'mapa_mental_mrv.html').read_bytes()
target = root / 'index.html'
if args.check:
    if target.read_bytes() != source:
        raise SystemExit('index.html desatualizado: execute python scripts/sync_site.py')
    print('HTML fonte e GitHub Pages sincronizados.')
else:
    target.write_bytes(source)
    print('index.html atualizado.')
