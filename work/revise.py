from pathlib import Path
import re,base64
s=Path('work/prototype.html').read_text()
s=s.replace('4 Fall Fishing Lures | Salt Strong','Salt Strong 2.0 | Fall Fishing Lures')
s=s.replace('A Salt Strong editorial prototype.','A Salt Strong WordPress article template concept.')
s=s.replace("fill='%23f3da25'","fill='%23152c52'").replace("font-size='22' text-anchor", "font-size='22' fill='white' text-anchor")
s=re.sub(r'<button class="cartbtn".*?</button>','<a class="login-link" href="https://www.saltstrong.com/member-login/" target="_blank" rel="noopener">Log in</a>',s,count=1)
s=s.replace('Join the Insider Club</a></div>','Join now</a></div>',1)
s=s.replace('Shop Tackle</a>','Tackle ↗</a>',1)
s=s.replace('LESS GUESSWORK. <span>MORE FISH.</span> THAT’S SALT STRONG.','CATCH MORE FISH. <span>MAKE MORE MEMORIES.</span>')
s=s.replace('<span class="eyebrow">FISH STRONG</span>','<span class="eyebrow tackle-badge">TACKLE BY FISH STRONG</span>')
s=s.replace('Like what Luke’s throwing? Put it in your tackle box.','Pick your gear here. Finish shopping at Fish Strong, our tackle store.')
s=re.sub(r'<div class="shelf-bottom">.*?</section>', '''<div class="shelf-bottom"><div><button class="select-all" data-select-all>Select all 4 lures</button><p><strong data-selection-summary>No gear selected</strong>Choose any of Luke’s four favorites.</p></div><button class="btn tackle" data-review disabled>Continue at Fish Strong ↗</button></div><p class="demo-note">Your article stays right here. Tackle purchases are completed on FishStrong.com.</p></section>''',s,count=1)
s=s.replace('Does “Add All” include the hooks and jigheads?','Does the four-lure lineup include rigging?').replace('No. It adds one of each of the four featured lure products, including one pack of each soft plastic. The Ultimate Fall Lure Bundle is a separate store offer that includes rigging.','The shelf features the four lures, with one pack of each soft plastic. The Ultimate Fall Lure Bundle at Fish Strong is a separate offer that also includes rigging.')
s=s.replace('Can I shop without leaving the article?','Where do I finish buying my tackle?').replace('You can try individual Add buttons, Add All, and quantity changes in this prototype. Nothing is sent to the store, and checkout is disabled. Live product and membership links open separately.','Pick the gear you like while reading, then continue to Fish Strong to finish shopping. Salt Strong is where you learn and plan your next trip. Fish Strong is our separate tackle store.')
s=s.replace('Editorial shopping concept','WordPress article template concept')
s=re.sub(r'<button class="btn dark wide" data-add-all.*?</section>', '''<button class="select-all wide" data-select-all style="margin-top:16px">Select all 4 lures</button><p class="sheet-status" data-sheet-status role="status" aria-live="polite"></p><p class="selection-summary" data-selection-summary>No gear selected</p><button class="btn tackle wide" data-review disabled>Continue at Fish Strong ↗</button><p class="demo-note">Tackle purchases are completed on FishStrong.com.</p></section>''',s,count=1)
s=re.sub(r'<dialog id="cart-dialog".*?</dialog>', '''<dialog id="gear-dialog" class="sheet" aria-labelledby="gear-title"><div class="dialog-head"><h2 id="gear-title">Your gear lineup</h2><button class="close" data-close aria-label="Close gear lineup">×</button></div><div class="dialog-body"><div class="handoff"><span class="tackle-badge">FISH STRONG</span><h3>Ready to gear up?</h3><p>You’re heading to our tackle store. Finish choosing your tackle and check out at FishStrong.com.</p></div><div id="gear-items"></div><div class="total"><span>Gear estimate</span><span id="subtotal">$0.00</span></div><p class="cartnote">Non-member prices shown. Confirm colors, sizes, availability, and Insider pricing at Fish Strong.</p><a class="btn tackle wide" href="https://fishstrong.com/" target="_blank" rel="noopener">Open Fish Strong ↗</a><p class="demo-note">Visual concept only: this link opens the store. Your selections are not transferred in this prototype.</p><button class="btn outline wide" data-close style="margin-top:14px">Keep reading on Salt Strong</button></div></dialog>''',s,count=1)
s=s.replace('Good gear.<br>Even better intel.','More fish.<br>More memories.')
s=s.replace('Know where to go, what to throw, and how to put it all together.','A fishing buddy in your corner. Local knowledge, proven lessons, and a community that helps you catch more fish.')
s=s.replace('Join the Insider Club <span','Join now <span')
# Brand-specific styles override the original visual concept without altering article structure.
css='''
/* Salt Strong WordPress template concept. Typography and palette from the 2023 brand guide. */
:root{--ink:#152c52;--muted:#566477;--line:#d6e0ea;--yellow:#d6e6f2;--soft:#f3f7fa;--sea:#152c52;--radius:8px;--tackle:#ca181e;--brand-gray:#a0a0a1}
body{font-family:Rubik,Arial,sans-serif;color:#26364b}h1,h2,h3{color:var(--ink)}
.topline{background:#d6e6f2;color:var(--ink);font-size:11px;letter-spacing:1.5px}.topline span{color:var(--ink)}
.header{background:var(--ink);border:0;color:white}.nav{min-height:86px;gap:26px}.brand,.brand img{width:204px;height:42px}.brand{padding:4px 0}.navlinks a{font-weight:400}.navlinks .active{font-weight:700;border-color:#d6e6f2}.login-link{font-size:13px;text-decoration:none;white-space:nowrap}.header .btn{background:#d6e6f2;color:var(--ink);font-weight:700;min-width:105px}.header .btn:hover{background:white}
.btn{background:var(--ink);color:white;border-radius:4px}.btn:hover,.btn.dark:hover{background:#234779}.btn.outline{background:white;color:var(--ink);border-color:#b9c9da}.btn.outline:hover{background:#edf3f8}
.article-head h1{font-family:'Salt Strong Sans',Rubik,sans-serif;font-weight:400;text-transform:uppercase;font-size:clamp(32px,3.7vw,50px);line-height:1.15;letter-spacing:0;max-width:1230px;margin:15px 0 20px}.article-head h1 span{background:none}.article-head:after{content:'';position:absolute;bottom:-2px;left:0;width:75px;height:4px;background:#152c52}.dek{font-size:18px;max-width:860px;line-height:1.7}.kicker{font-family:Rubik,Arial,sans-serif;font-weight:700}.byline{font-size:12px}.byline strong{font-weight:700}.playcircle{background:#fff;color:var(--ink)}
.sectiontitle h2{font-family:'Salt Strong Serif',Rubik,sans-serif;letter-spacing:0;font-size:21px;text-transform:uppercase;font-weight:400}.shelf{border-top:3px solid #152c52;background:white}.sectiontitle{align-items:start}.sectiontitle .tackle-badge{font-size:10px;color:var(--tackle);letter-spacing:.8px;text-align:right;max-width:125px;line-height:1.4}.tackle-badge{font-size:12px;font-weight:700;color:var(--tackle);letter-spacing:1px}.tackle-badge:before{content:'';display:inline-block;width:7px;height:7px;background:var(--tackle);margin-right:6px}
.shelf-intro{font-size:13px;line-height:1.6;max-width:590px}.product-photo{background:#f5f7f9}.product h3{font-weight:700;font-size:14px}.product .type{font-size:10px}.price small{color:#536579;font-size:11px}.add{border-color:#b9c9da;color:var(--ink);font-weight:500}.add:hover{background:#edf3f8;border-color:#152c52}.add[aria-pressed=true]{background:#d6e6f2;border-color:#152c52;font-weight:700}.select-all{padding:0;background:none;color:var(--ink);font-size:13px;font-weight:700;text-decoration:underline;text-underline-offset:4px;min-height:36px}.shelf-bottom{align-items:center}.shelf-bottom strong{font-size:14px}.shelf-bottom p{font-size:12px}.tackle{background:#ca181e;color:white;font-size:13px;white-space:normal}.tackle:hover{background:#a71419}.tackle:disabled{opacity:1;background:#e8edf3;color:#626f7e}.demo-note{font-size:11px;line-height:1.65}.selection-summary{font-size:13px;margin:5px 0 12px}.handoff{padding:18px;background:#f3f7fa;border-radius:7px;border-left:3px solid #ca181e}.handoff h3{font-size:22px;margin:10px 0}.handoff p{font-size:14px;line-height:1.7}.cartrow{grid-template-columns:65px 1fr auto}.cartrow a{color:#152c52;font-weight:700;text-decoration:none}.cartrow a:hover{text-decoration:underline}
.lesson h2{font-family:'Salt Strong Serif',Rubik,sans-serif;font-size:23px;font-weight:400;letter-spacing:0;text-transform:uppercase;line-height:1.25}.lesson .sub{font-size:12px;letter-spacing:.4px}.lesson p{font-size:16px;line-height:1.9}.number{background:#d6e6f2;border-radius:5px;color:#152c52}.tip{background:#f3f7fa;border-left-color:#152c52;font-size:14px;line-height:1.8}.jump a{font-size:11px}.jump a:hover{background:#d6e6f2}.rig-heading{background:#d6e6f2}.rig-heading h2{font-family:'Salt Strong Serif',Rubik,sans-serif;font-size:21px;letter-spacing:0;line-height:1.2;font-weight:400;text-transform:uppercase}.rig-heading .kicker{font-size:10px}.rig-tip{background:#edf3f8}.rig-line strong{font-size:13px}.rig-line p{font-size:12px}.rig-body{padding:17px}.rig-foot{font-size:11px}.mode button{font-size:11px}.rail{top:108px;max-height:calc(100dvh - 126px)}
.club{background:#152c52;padding:23px}.club h2{font-family:'Salt Strong Sans',Rubik,sans-serif;font-size:25px;line-height:1.2;letter-spacing:0;font-weight:400;text-transform:uppercase;color:white}.club .kicker{color:#d6e6f2;font-size:10px}.club p{font-size:13px;color:#d6e6f2}.club li:before{color:#d6e6f2}.club .btn{background:#d6e6f2;color:#152c52}.club .btn:hover{background:white}.club ul{font-size:12px}.bundle h3,.faq h2{font-family:'Salt Strong Serif',Rubik,sans-serif;font-weight:400;font-size:22px;letter-spacing:0}.bundle .btn{color:#ca181e;border-color:#ddbac0}.total{font-size:17px}.dialog-head h2{font-family:'Salt Strong Serif',Rubik,sans-serif;font-weight:400;font-size:22px;letter-spacing:0}.footer{font-size:11px}.sheet-status{color:#152c52}.toast{background:#152c52}
@media(max-width:1100px){.nav{gap:20px}.brand,.brand img{width:175px}.navlinks{gap:18px}.article-head h1{font-size:40px}.shelf-bottom{flex-wrap:wrap}.sectiontitle h2{font-size:19px}}
@media(max-width:800px){.nav{padding:13px 20px;min-height:72px;gap:12px}.brand,.brand img{width:164px;height:32px}.header .btn{min-width:82px;padding:10px;font-size:12px}.login-link{display:none}.topline{font-size:9px;padding:7px 8px}.article-head h1{font-size:clamp(25px,6.8vw,37px);line-height:1.2;letter-spacing:0}.article-head h1 br{display:none}.article-head h1 span:before{content:' '}.dek{font-size:16px}.sectiontitle h2{font-size:18px;line-height:1.25}.sectiontitle .tackle-badge{max-width:85px;font-size:9px;flex-shrink:0}.shelf-intro{font-size:12px}.product{flex-basis:160px}.product h3{font-size:14px}.lesson h2{font-size:21px}.shelf-bottom{align-items:stretch}.shelf-bottom .btn{width:100%}.mobilebar{border-top:2px solid #152c52;box-shadow:0 -4px 20px #152c5214}.mobilebar .btn{background:#152c52;color:white;min-width:135px}.mobilebar strong{color:#152c52}.mobilebar small{font-size:10px}.bundle{grid-template-columns:75px 1fr}.bundle h3{font-size:18px}.bundle img{width:75px}.rig-heading h2{font-size:22px}.club h2{font-size:27px}.sheet .dialog-body>section{min-width:0}.cartrow{grid-template-columns:50px 1fr auto}.video-dialog .dialog-head h2{font-size:18px}}
'''
fonts=[('Salt Strong Sans','Salt Strong Sans.otf','opentype',400),('Salt Strong Serif','Salt Strong Serif.otf','opentype',400),('Rubik','Rubik-Regular.ttf','truetype',400),('Rubik','Rubik-Bold.ttf','truetype',700)]
fontcss=''
for family,file,fmt,weight in fonts:
 data=base64.b64encode((Path('/Users/alex/Library/Fonts')/file).read_bytes()).decode()
 mime='font/otf' if fmt=='opentype' else 'font/ttf'
 fontcss+=f"@font-face{{font-family:'{family}';src:url(data:{mime};base64,{data}) format('{fmt}');font-weight:{weight};font-style:normal;font-display:swap;}}\n"
s=s.replace('</style>',fontcss+css+'</style>',1)
# Replace shopping-cart behavior with a local gear-selection preview.
start=s.index('const cart=new Map();')
end=s.index('let dialogTrigger=null;',start)
s=s[:start]+'''const selected=new Set(); let toastTimer; let mode='shallow';
const productPaths={moonwalker:'moonwalker',skinny:'skinny-lipper-xl',bomber:'the-mulligan-bomber-5',prawn:'power-prawn-usa-original'};
function productHTML(p){return `<article class="product"><div class="product-photo"><img src="${p.img}" alt="${p.name}" loading="lazy"></div><div class="type">${p.type}</div><h3>${p.name}</h3><p class="variant">${p.variant}</p><p class="price">${money(p.price)}<small>${money(p.insider)} Insider price</small></p><button class="add" data-select="${p.id}" aria-pressed="false" aria-label="Select ${p.name}">+ Select</button></article>`;}
['products','mobile-products'].forEach(id=>document.getElementById(id).innerHTML=products.map(productHTML).join(''));
['desktop-rig','mobile-rig'].forEach(id=>document.getElementById(id).append(document.getElementById('rig-template').content.cloneNode(true)));
['desktop-club','mobile-club'].forEach(id=>document.getElementById(id).append(document.getElementById('club-template').content.cloneNode(true)));
function notify(message){const t=document.getElementById('toast');clearTimeout(toastTimer);t.textContent=message;document.querySelectorAll('[data-sheet-status]').forEach(el=>el.textContent=message);t.classList.add('show');toastTimer=setTimeout(()=>t.classList.remove('show'),2600)}
function renderSelection(){
 const items=products.filter(p=>selected.has(p.id));
 const sum=items.reduce((n,p)=>n+p.price,0);
 document.querySelectorAll('[data-select]').forEach(b=>{const yes=selected.has(b.dataset.select);b.setAttribute('aria-pressed',String(yes));b.textContent=yes?'✓ Selected':'+ Select';});
 document.querySelectorAll('[data-select-all]').forEach(b=>b.textContent=selected.size===products.length?'Clear selection':'Select all 4 lures');
 document.querySelectorAll('[data-review]').forEach(b=>b.disabled=!items.length);
 document.querySelectorAll('[data-selection-summary]').forEach(e=>e.textContent=items.length?`${items.length} selected · ${money(sum)}`:'No gear selected');
 document.getElementById('gear-items').innerHTML=items.map(p=>`<div class="cartrow"><img src="${p.img}" alt=""><div><h3><a href="https://fishstrong.com/products/${productPaths[p.id]}" target="_blank" rel="noopener">${p.name} ↗</a></h3><p>${p.variant}</p></div><strong>${money(p.price)}</strong></div>`).join('');
 document.getElementById('subtotal').textContent=money(sum);
}
''' + s[end:]
s=s.replace("else document.querySelector('.cartbtn').focus();","else document.querySelector('#featured [data-review]').focus();")
start=s.index("document.addEventListener('click',e=>")
end=s.index("document.getElementById('play-video')",start)
s=s[:start]+'''document.addEventListener('click',e=>{
 const b=e.target.closest('button');if(!b)return;
 if(b.hasAttribute('data-select')){const id=b.dataset.select;selected.has(id)?selected.delete(id):selected.add(id);renderSelection();notify(`${products.find(p=>p.id===id).name} ${selected.has(id)?'selected':'removed'}`);}
 if(b.hasAttribute('data-select-all')){if(selected.size===products.length)selected.clear();else products.forEach(p=>selected.add(p.id));renderSelection();notify(selected.size?'All 4 lures selected. Continue at Fish Strong when you’re ready.':'Gear selection cleared');}
 if(b.hasAttribute('data-review')&&selected.size)openDialog('gear-dialog',b);
 if(b.hasAttribute('data-open-rig'))openDialog('rig-dialog',b);
 if(b.hasAttribute('data-close'))b.closest('dialog').close();
 if(b.hasAttribute('data-mode'))setMode(b.dataset.mode);
 if(b.hasAttribute('data-rig-link'))window.open(mode==='deep'?'https://fishstrong.com/products/hoss-round-eye-jig-head':'https://fishstrong.com/products/salt-strong-hoss-helix-hooks','_blank','noopener');
});
''' + s[end:]
s=s.replace('renderCart();','renderSelection();')
# Preserve the original deliverable for comparison and publish the brand revision separately.
Path('work/prototype-v2.html').write_text(s)
embed=Path('work/embed.py').read_text().replace("Path('work/prototype.html')","Path('work/prototype-v2.html')").replace("'outputs/salt-strong-blog-prototype.html'","'outputs/salt-strong-blog-v2.html'")
embed=embed.replace("s=s.replace('@@'+key+'@@','data:'+mime+';base64,'+base64.b64encode((base/path).read_bytes()).decode())","s=s.replace('@@'+key+'@@','data:'+mime+';base64,'+base64.b64encode((base/path).read_bytes()).decode())" )
# Replace the logo placeholder before the standard image embedding stage.
svg=base64.b64encode(Path('/Users/alex/Downloads/SaltStrong_Primary_Horz_White.svg').read_bytes()).decode()
s=s.replace('@@logo@@','data:image/svg+xml;base64,'+svg)
Path('work/prototype-v2.html').write_text(s)
Path('work/embed-v2.py').write_text(embed)
