from pathlib import Path
import base64
base=Path('/var/folders/zy/hc9bxc9s6nl_p668wzndjkx00000gn/T/browser-use/assets')
assets={
'logo':('b997fa9b-706f-46a1-ba53-649681ce8820/6a84f4dcf09a4817.png','image/png'),
'author':('b997fa9b-706f-46a1-ba53-649681ce8820/a3e11e2e4c5d5783','image/jpeg'),
'video':('f70760a5-7855-4453-914d-e1c135ddb4fc/c2dbb058a6985d64.jpg','image/jpeg'),
'bundle':('f70760a5-7855-4453-914d-e1c135ddb4fc/0776d2845337ab48.png','image/webp'),
'moon':('8f0846dc-4fc8-4f69-b575-307a0fadf387/d8e75e0da94c7bc0.png','image/webp'),
'skinny':('6c73fa19-08e8-467d-9890-c15c79f97522/f12995a580549a71.jpg','image/webp'),
'bomber':('ee381050-96f4-4b60-9c2f-aa4eccb4789a/bdbb5a6679364cbc.png','image/webp'),
'prawn':('d52eba51-2db7-4556-98a5-4d0a74cdb943/bb20acfe40a64052.png','image/avif')}
s=Path('work/prototype-v2.html').read_text()
for key,(path,mime) in assets.items():
    s=s.replace('@@'+key+'@@','data:'+mime+';base64,'+base64.b64encode((base/path).read_bytes()).decode())
assert '@@' not in s
assert '\u2014' not in s
Path('outputs/salt-strong-blog-v2.html').write_text(s)
print('Self-contained HTML:',len(s),'bytes')
