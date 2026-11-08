"""Cache-busting: give each asset link in index.html a version taken from the file's content,
so phones always fetch the new app.js / data.js / app.css together after an update.
Run after build_v4.py: python3 tools/stamp.py"""
import hashlib, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, 'index.html'); s = open(p).read()
def stamp(m):
    f = m.group(1); h = hashlib.md5(open(os.path.join(ROOT, f), 'rb').read()).hexdigest()[:8]
    return '%s?v=%s' % (f, h)
s = re.sub(r'(assets/(?:app\.css|app\.js|data\.js|config\.js))\?v=[\w.]+', stamp, s)
open(p, 'w').write(s); print(re.findall(r'assets/[\w.]+\?v=\w+', s))
