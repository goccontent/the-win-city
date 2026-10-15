# Kiểm tra: mọi ảnh images/... được index.html tham chiếu đều tồn tại. Chạy: python check.py
import re, os
html = open('index.html', encoding='utf-8').read()
refs = set(re.findall(r"images/[\w.-]+\.(?:jpg|png)", html))
refs |= {f"images/{f}.jpg" for f in re.findall(r"\['([\w-]+)','", html.split('const GALLERY')[1].split('];')[0])}
missing = sorted(r for r in refs if not os.path.exists(r))
assert not missing, missing
print(f"OK {len(refs)} ảnh")

# Chiết tính: mỗi phương thức thanh toán cộng đủ 100%, phần ngân hàng 0% hoặc 70%
import json
plans = json.loads(html.split('/*PLANS*/')[1].split('/*END*/')[0])
for k, rows in plans.items():
    assert abs(sum(r[2] * r[3] for r in rows) - 1) < 1e-9, k
    assert round(sum(r[2] * r[3] for r in rows if r[4] == 'nh'), 9) in (0, 0.7), k
print(f"OK {len(plans)} phương thức thanh toán")
