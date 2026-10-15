# Kiểm tra: mọi ảnh images/... được index.html tham chiếu đều tồn tại. Chạy: python check.py
import re, os
html = open('index.html', encoding='utf-8').read()
refs = set(re.findall(r"images/[\w.-]+\.(?:jpg|png)", html))
refs |= {f"images/{f}.jpg" for f in re.findall(r"\['([\w-]+)','", html.split('const GALLERY')[1].split('];')[0])}
missing = sorted(r for r in refs if not os.path.exists(r))
assert not missing, missing
print(f"OK {len(refs)} ảnh")
