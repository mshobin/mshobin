"""Checks every relative link and heading anchor in the repository's Markdown files.

Run: python tools/check_doc_links.py      Exit code 0 = every link and #anchor resolves.
Web links (http, https, mailto) are not fetched. templates/ is skipped. Anchors follow GitHub's heading rules.
"""
import re, pathlib, subprocess, sys, unicodedata
root = pathlib.Path(__file__).resolve().parent.parent
files = [root / f for f in subprocess.check_output(['git', 'ls-files', '-co', '--exclude-standard', '*.md'], cwd=root).decode().split()
         if not f.startswith('templates/')]  # templates link to files in the repo they are copied into
def slug(t):
    t = re.sub(r'<[^>]+>', '', t).strip().lower()
    t = re.sub(r'[`*_~\[\]()]', '', t)
    t = ''.join(c for c in t if c.isalnum() or c in ' -' or unicodedata.category(c).startswith('L'))
    return t.replace(' ', '-')
anchors = {}
def anchors_of(p):
    if p not in anchors:
        s = p.read_text(encoding='utf-8'); seen = {}; out = set()
        s = re.sub(r'```.*?```', '', s, flags=re.S)
        for m in re.finditer(r'^#{1,6}\s+(.*)$', s, flags=re.M):
            a = slug(m.group(1)); n = seen.get(a, 0); seen[a] = n + 1
            out.add(a if n == 0 else f'{a}-{n}')
        for m in re.finditer(r'<a\s+(?:name|id)="([^"]+)"', s): out.add(m.group(1))
        anchors[p] = out
    return anchors[p]
bad = 0
for f in files:
    s = f.read_text(encoding='utf-8')
    body = re.sub(r'```.*?```', '', s, flags=re.S)
    links = re.findall(r'\]\(([^)\s]+)\)', body) + re.findall(r'(?:src|href)="([^"]+)"', body)
    for l in links:
        if re.match(r'^(https?:|mailto:)', l): continue
        path, _, anc = l.partition('#')
        tgt = (f.parent / path).resolve() if path else f
        if not tgt.exists():
            print(f'{f.relative_to(root)}: missing {l}'); bad += 1; continue
        if anc and tgt.suffix == '.md' and anc not in anchors_of(tgt):
            print(f'{f.relative_to(root)}: no anchor #{anc} in {tgt.relative_to(root)}'); bad += 1
print(f'{len(files)} files, {bad} problems'); sys.exit(1 if bad else 0)
