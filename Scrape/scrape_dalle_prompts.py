from bs4 import BeautifulSoup

def extract_from_html(html_content):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text from H3 span tags
    h3_texts = [h3.text for h3 in soup.find_all('h3')]
    
    # Extract text from strong tags
    strong_texts = [strong.text for strong in soup.find_all('strong')]
    
    return h3_texts, strong_texts

def extract_img_alt(html_content):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract alt texts from img tags
    alt_texts = [img['alt'] for img in soup.find_all('img') if img.has_attr('alt')]
    
    return alt_texts

def fmt(s):
    return s.replace("”", "\"").replace("“", "\"").strip()

def fmt1(s):
    if s.startswith("A "):
        return s[2:].strip()
    else:
        return s.replace("”", "\"").replace("“", "\"").strip()

def qt(s):
    return '\"' + s.strip() + '\"'

repeat = {}

def first_word(s):
    s2 = s.replace(',', '')
    words = s2.split()
    i = 0
    w = words[i]
    while len(w) < 2:
        i += 1
        w = words[i]
    if w in repeat:
        repeat[w] = repeat[w] + 1
        w = w + str(repeat[w])
    else:
        repeat[w] = 1
    return w


if __name__ == "__main__":
    # Provided HTML content
    html_content = '''

							<img loading="lazy" src="/dynimg/ef-8o51NGk-Do2P44y4SYl1zCldU10qYCpmzbM5hLF0/w:400/Y29udGVudC9pbWFnZXMvZGFkZWFkNzkzZjY0ZTAwN2JkYjhiYjgzZDI4M2FmMTQ4NjBkMjViZTNjZTRmZGI1N2I3NDVlYTg2ZjM3OTZiNy5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical" data-image-id="dadead793f64e007bdb8bb83d283af14860d25be3ce4fdb57b745ea86f3796b7" style="cursor: pointer;">
			<img loading="lazy" src="/dynimg/sFfdz0rhmi4F6G-gE6UvMv69Bh-_jCvsyPVSg-N_I1w/w:400/Y29udGVudC9pbWFnZXMvM2MwMTk0NTAxYThlZGMzNzI0NGE3YTYwMjI3YzY4MjczNmVjYjhjZDA1NTRlZmUzZmVmZThkN2UzOWIxOWMwMy5wbmc" alt="A wolf in sheeps clothing, AMOLED wallpaper, avatar, digital art" title="A wolf in sheeps clothing, AMOLED wallpaper, avatar, digital art" data-image-id="3c0194501a8edc37244a7a60227c682736ecb8cd0554efe3fefe8d7e39b19c03" style="cursor: pointer;">
			<img loading="lazy" src="/dynimg/d2bJtebRc4hmBD95LAoNPcS3XFViWEoU12gtRypnS4M/w:400/Y29udGVudC9pbWFnZXMvNDk3Yjg2NmEwNWI2NDRkNDMwYWUzOTU0YWZkY2ViOThiYTE5MTViZTU2NWI0Y2NlNjU1OThkNWZkNjY1NmMyOC5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical" data-image-id="497b866a05b644d430ae3954afdceb98ba1915be565b4cce65598d5fd6656c28" style="cursor: pointer;">
			<img loading="lazy" src="/dynimg/-esfFiTgIJbPvtXJ_o5JiqCQr1KXtwC7fu-zzI6wBVc/w:400/Y29udGVudC9pbWFnZXMvNGU5MGM3M2UzOGUzNjViOWExNzZlOTc2OGRkNjMxYjM0ZjIyMjcyYWM1ZDE4YWIzOWVhNGNiYjY2MTVmNmM0Ny5wbmc" alt="Dragon made of fire, AMOLED wallpaper" title="Dragon made of fire, AMOLED wallpaper" data-image-id="4e90c73e38e365b9a176e9768dd631b34f22272ac5d18ab39ea4cbb6615f6c47" style="cursor: pointer;">
		</div>

<div style="display: flex; gap: 1em; align-items: center;">
	<h1 style="flex: 0 auto; margin-bottom: 0;">
					<i class="fa fa-i-cursor" title="Prompt" style="color:#e91088;"></i> <span class="page-prompt-title" style="color:#000;">AMOLED wallpaper</span>
			</h1>
	<button
		type="button"
		onclick="
			navigator.clipboard.writeText(document.querySelector('.page-prompt-title').textContent)
			.then(() => {
				this.firstElementChild.classList.remove('fa-clone');
				this.firstElementChild.classList.add('fa-check');
				setTimeout(() => this.firstElementChild.classList.replace('fa-check', 'fa-clone'), 1500);
			});"
		title="Copy to clipboard"
		style="all: unset; flex: none; color:#e91088; cursor: pointer; font-size: 20px;"
		>
		<i class="fa fa-clone"></i>
	</button>
</div>

<div style="display: flex; gap: 0.5em; margin-top:1em;">
		<div class="article-page-desc" >
		Discover artwork inspired by this prompt or request new artwork to suit your needs.	</div>
</div>

<div class="contentcontainer_sub">
					<div
	class="item-reactions"
			data-item="{&quot;item_type&quot;:&quot;article&quot;,&quot;item_id&quot;:&quot;prompt:amoled-wallpaper&quot;}"
				id="page-reaction"
		>
			<button type="button" class="reaction" data-reaction="👍">
			<span>👍</span>
			<span class="count">58</span>
		</button>
			<button type="button" class="reaction" data-reaction="❤️">
			<span>❤️</span>
			<span class="count">34</span>
		</button>
			<button type="button" class="reaction" data-reaction="⭐️">
			<span>⭐️</span>
			<span class="count">34</span>
		</button>
		<button type="button" class="add">+</button>
</div>
	

	
	
	<hr class="hrulethin">

	</div>

<div style="margin-top:2em; margin-bottom:2em;">
		
<div><h3>DALL·E generated artwork using this prompt.</h3></div>
	<div style="display: flex; flex-wrap: wrap; gap: 1em; align-items: start; justify-content: space-between;">
					<aside class="image-sort-dropdown" style="display: inline-flex; flex-wrap: wrap; gap: 1em;">
	<form style="display: contents;">
				<select name="sort" onchange="this.closest('form').submit()" style="padding:1em; font-size:16px; background-color:#fafafa; color:#444; border:1px solid #ddd; border-radius:1em; width:100%; font-weight: bold;">
							<option value="rand" selected>Featured</option>
						<option value="recent" >Most Recent</option>
			<option value="liked" >Most Liked</option>
		</select>
	</form>
</aside>
			</div>
</div>



		<div
		class="image-list scroll-list"
		data-base-url="?ajax=1&rkey=1801370639&page="
		data-pages-offset="1"
		data-pages-total="2"
		>
		<template id="item-reactions-template"><div
	class="item-reactions"
			>
			<button type="button" class="reaction" data-reaction="">
			<span></span>
			<span class="count"></span>
		</button>
		<button type="button" class="add">+</button>
</div>
</template><dialog id="image-viewer-dialog" >
	<img class="image" style="--loading-text: 'Loading...';">
	<div class="pane">
		<div class="actions">
			<button
				type="button"
									class="delete"
					style="display: none;"
								><i class="fa fa-trash"></i></button>
			<a class="download" rel="nofollow">
				<button type="button" disabled><i class="fa fa-download"></i></button>
			</a>
			<button type="button" class="close"><i class="fa fa-close"></i></button>
		</div>
		<div class="details">
			<p class="prompt"></p>
			<div class="uploader" style="display: none;">
				<i class="fa fa-user" title="Uploader"></i>
				<a class="user" rel="nofollow"></a>
			</div>
		</div>
	</div>
</dialog>
<div class="image-item" data-image-id="252ba7750f839dd8a80590437774a4e5061da2443c6b3a86a3dd306c62f1b281">
	<div class="top">
		<img loading="lazy" src="/dynimg/dgMOR3WNm815Bc40JDxOLOLzlCYM2HDfDwMUzbrDTK4/w:400/Y29udGVudC9pbWFnZXMvMjUyYmE3NzUwZjgzOWRkOGE4MDU5MDQzNzc3NGE0ZTUwNjFkYTI0NDNjNmIzYTg2YTNkZDMwNmM2MmYxYjI4MS5wbmc" alt="Dragon made of fire, AMOLED wallpaper, logo mascot" title="Dragon made of fire, AMOLED wallpaper, logo mascot">
		<div class="desc">
							&quot;Dragon made of fire, <b>AMOLED wallpaper</b>, logo mascot&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="dadead793f64e007bdb8bb83d283af14860d25be3ce4fdb57b745ea86f3796b7">
	<div class="top">
		<img loading="lazy" src="/dynimg/ef-8o51NGk-Do2P44y4SYl1zCldU10qYCpmzbM5hLF0/w:400/Y29udGVudC9pbWFnZXMvZGFkZWFkNzkzZjY0ZTAwN2JkYjhiYjgzZDI4M2FmMTQ4NjBkMjViZTNjZTRmZGI1N2I3NDVlYTg2ZjM3OTZiNy5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical">
		<div class="desc">
							&quot;gundam, <b>AMOLED wallpaper</b>, mystical&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="5f3685a3a6bf6520018d6378007966871015360346123d39a1ac14610c8cce07">
	<div class="top">
		<img loading="lazy" src="/dynimg/Sl7s1SfjGuTc25IfLvnYRHSu2QtntKJK7Wrmn0SX5pE/w:400/Y29udGVudC9pbWFnZXMvNWYzNjg1YTNhNmJmNjUyMDAxOGQ2Mzc4MDA3OTY2ODcxMDE1MzYwMzQ2MTIzZDM5YTFhYzE0NjEwYzhjY2UwNy5wbmc" alt="Dragon made of fire, AMOLED wallpaper" title="Dragon made of fire, AMOLED wallpaper">
		<div class="desc">
							&quot;Dragon made of fire, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="6913318049af972ba598870b101163c092de779b0141c09389f73b679b281ffb">
	<div class="top">
		<img loading="lazy" src="/dynimg/BDA0gUj9so63ur93vtJFYPg114kTIqn1wC3XdHPWBGk/w:400/Y29udGVudC9pbWFnZXMvNjkxMzMxODA0OWFmOTcyYmE1OTg4NzBiMTAxMTYzYzA5MmRlNzc5YjAxNDFjMDkzODlmNzNiNjc5YjI4MWZmYi5wbmc" alt="Monsters, AMOLED wallpaper, digital art" title="Monsters, AMOLED wallpaper, digital art">
		<div class="desc">
							&quot;Monsters, <b>AMOLED wallpaper</b>, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="2a16e8cb85ea38a0c3c7733a052930bf595b57b4d765d9b1442ab2353c1f9376">
	<div class="top">
		<img loading="lazy" src="/dynimg/esvBBSR7Z4v0GJRYf09UOENfb8cZiVcNZhle_QjyXRI/w:400/Y29udGVudC9pbWFnZXMvMmExNmU4Y2I4NWVhMzhhMGMzYzc3MzNhMDUyOTMwYmY1OTViNTdiNGQ3NjVkOWIxNDQyYWIyMzUzYzFmOTM3Ni5wbmc" alt="Blueprint of cartoon character, Cally3D, 3D, schematic, digital art, inner glow, AMOLED wallpaper" title="Blueprint of cartoon character, Cally3D, 3D, schematic, digital art, inner glow, AMOLED wallpaper">
		<div class="desc">
							&quot;Blueprint of cartoon character, Cally3D, 3D, schematic, digital art, inner glow, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="4a5377d76e6b705f3bc5ad360df101ec6d64be712a9ee4668cf392c8345526de">
	<div class="top">
		<img loading="lazy" src="/dynimg/KaWaPXDIqaDm5YKqaU6DR0zM3jUYIc9JxrUWA6HpK-o/w:400/Y29udGVudC9pbWFnZXMvNGE1Mzc3ZDc2ZTZiNzA1ZjNiYzVhZDM2MGRmMTAxZWM2ZDY0YmU3MTJhOWVlNDY2OGNmMzkyYzgzNDU1MjZkZS5wbmc" alt="Fox, kaleidoscope, AMOLED wallpaper" title="Fox, kaleidoscope, AMOLED wallpaper">
		<div class="desc">
							&quot;Fox, kaleidoscope, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="497b866a05b644d430ae3954afdceb98ba1915be565b4cce65598d5fd6656c28">
	<div class="top">
		<img loading="lazy" src="/dynimg/d2bJtebRc4hmBD95LAoNPcS3XFViWEoU12gtRypnS4M/w:400/Y29udGVudC9pbWFnZXMvNDk3Yjg2NmEwNWI2NDRkNDMwYWUzOTU0YWZkY2ViOThiYTE5MTViZTU2NWI0Y2NlNjU1OThkNWZkNjY1NmMyOC5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical">
		<div class="desc">
							&quot;gundam, <b>AMOLED wallpaper</b>, mystical&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="0d2d1b87b9c95fe3cefef797fd8d696d4b15bed5d2e90f0927ad1ac9a86effe9">
	<div class="top">
		<img loading="lazy" src="/dynimg/X7cw2-xM19elZfMrwuictlA3ffmRyL3hrYKmCuurgfg/w:400/Y29udGVudC9pbWFnZXMvMGQyZDFiODdiOWM5NWZlM2NlZmVmNzk3ZmQ4ZDY5NmQ0YjE1YmVkNWQyZTkwZjA5MjdhZDFhYzlhODZlZmZlOS5wbmc" alt="A wolf in sheeps clothing, AMOLED wallpaper, avatar, digital art" title="A wolf in sheeps clothing, AMOLED wallpaper, avatar, digital art">
		<div class="desc">
							&quot;A wolf in sheeps clothing, <b>AMOLED wallpaper</b>, avatar, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="3b47b27658e560cf89792cc8673774e37b6f8b177d41d46eb7b47b57da7486f5">
	<div class="top">
		<img loading="lazy" src="/dynimg/0zyNvOeDy4ShX9Ndjcoe42012dF3lOPZi5KjORz6rG4/w:400/Y29udGVudC9pbWFnZXMvM2I0N2IyNzY1OGU1NjBjZjg5NzkyY2M4NjczNzc0ZTM3YjZmOGIxNzdkNDFkNDZlYjdiNDdiNTdkYTc0ODZmNS5wbmc" alt="Golden retriever, AMOLED wallpaper, op art" title="Golden retriever, AMOLED wallpaper, op art">
		<div class="desc">
							&quot;Golden retriever, <b>AMOLED wallpaper</b>, op art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="bf5472f0e84af6e97186e1dd464c60acb1950b2fdfbfd5617116e415ce0f24d0">
	<div class="top">
		<img loading="lazy" src="/dynimg/g-YnIsF6tXcOUnwZxgxQKnoyM-10KkvSCdcANOIJGGg/w:400/Y29udGVudC9pbWFnZXMvYmY1NDcyZjBlODRhZjZlOTcxODZlMWRkNDY0YzYwYWNiMTk1MGIyZmRmYmZkNTYxNzExNmU0MTVjZTBmMjRkMC5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical">
		<div class="desc">
							&quot;gundam, <b>AMOLED wallpaper</b>, mystical&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="f34a25eb375472aa96032df3b8e4c15a59b4dc29e12ed2c038bce7a88f56e158">
	<div class="top">
		<img loading="lazy" src="/dynimg/B5R_zh5ughCU_u0pVs06bK7jQfHVAazMEaBSlF9o9qI/w:400/Y29udGVudC9pbWFnZXMvZjM0YTI1ZWIzNzU0NzJhYTk2MDMyZGYzYjhlNGMxNWE1OWI0ZGMyOWUxMmVkMmMwMzhiY2U3YTg4ZjU2ZTE1OC5wbmc" alt="Golden retriever, AMOLED wallpaper, op art" title="Golden retriever, AMOLED wallpaper, op art">
		<div class="desc">
							&quot;Golden retriever, <b>AMOLED wallpaper</b>, op art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="523af0e17daaf9caaefc7872af131b08e92c7cd7827f190ba860babcc1265f91">
	<div class="top">
		<img loading="lazy" src="/dynimg/XpNhQ_jd6QGCba42-EjnOX-gx2ksBa2n8hpqLwI5roM/w:400/Y29udGVudC9pbWFnZXMvNTIzYWYwZTE3ZGFhZjljYWFlZmM3ODcyYWYxMzFiMDhlOTJjN2NkNzgyN2YxOTBiYTg2MGJhYmNjMTI2NWY5MS5wbmc" alt="Golden retriever, AMOLED wallpaper, digital art" title="Golden retriever, AMOLED wallpaper, digital art">
		<div class="desc">
							&quot;Golden retriever, <b>AMOLED wallpaper</b>, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="48d0575a090979fea4ea4845b8a5d4f475c14ebe92df67813456bc7a99d22544">
	<div class="top">
		<img loading="lazy" src="/dynimg/Ltj1-IqFt7K8cO-AENFlbih30YPMR7etNJcLq2A1nvg/w:400/Y29udGVudC9pbWFnZXMvNDhkMDU3NWEwOTA5NzlmZWE0ZWE0ODQ1YjhhNWQ0ZjQ3NWMxNGViZTkyZGY2NzgxMzQ1NmJjN2E5OWQyMjU0NC5wbmc" alt="A wolf in sheeps clothing, AMOLED wallpaper, avatar, op art, digital art" title="A wolf in sheeps clothing, AMOLED wallpaper, avatar, op art, digital art">
		<div class="desc">
							&quot;A wolf in sheeps clothing, <b>AMOLED wallpaper</b>, avatar, op art, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="fc85e6e54a7e2956ca98b360ada26d8e4e65dd20d168cbe83184f44812e6f014">
	<div class="top">
		<img loading="lazy" src="/dynimg/waizKD9-ahj9i1mCZgWFVskXYdmVYVgFF8oe5eiiXik/w:400/Y29udGVudC9pbWFnZXMvZmM4NWU2ZTU0YTdlMjk1NmNhOThiMzYwYWRhMjZkOGU0ZTY1ZGQyMGQxNjhjYmU4MzE4NGY0NDgxMmU2ZjAxNC5wbmc" alt="gundam, colorful splash, abstract, amoled wallpaper" title="gundam, colorful splash, abstract, amoled wallpaper">
		<div class="desc">
							&quot;gundam, colorful splash, abstract, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="896f35f7a8aff4bd8269af0f6a1c321c7c4a7e1fbbad0a65b82331bc858aabab">
	<div class="top">
		<img loading="lazy" src="/dynimg/nK7WrE_u0KH8oPIHbdcjYBAMcqfeDTNdhucxuKX_eHI/w:400/Y29udGVudC9pbWFnZXMvODk2ZjM1ZjdhOGFmZjRiZDgyNjlhZjBmNmExYzMyMWM3YzRhN2UxZmJiYWQwYTY1YjgyMzMxYmM4NThhYWJhYi5wbmc" alt="Underwater Monsters, AMOLED wallpaper" title="Underwater Monsters, AMOLED wallpaper">
		<div class="desc">
							&quot;Underwater Monsters, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="16cba959847bcf1739e03dc59916a00f86ef82962e42d48003a48cf498538d18">
	<div class="top">
		<img loading="lazy" src="/dynimg/3jiYmILa8BKRvi5xS4GVZsPIbV0ECGHV23gVZqR1UZM/w:400/Y29udGVudC9pbWFnZXMvMTZjYmE5NTk4NDdiY2YxNzM5ZTAzZGM1OTkxNmEwMGY4NmVmODI5NjJlNDJkNDgwMDNhNDhjZjQ5ODUzOGQxOC5wbmc" alt="Fox, kaleidoscope, AMOLED wallpaper" title="Fox, kaleidoscope, AMOLED wallpaper">
		<div class="desc">
							&quot;Fox, kaleidoscope, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="db137edf2f2aba060fcccd4f5e0d1e8f8f60d7e74a5129287497957f8656c528">
	<div class="top">
		<img loading="lazy" src="/dynimg/nV8nDkUY-KG_pxKcwWVGd1k3FtJUedOIAVtZnMRduMM/w:400/Y29udGVudC9pbWFnZXMvZGIxMzdlZGYyZjJhYmEwNjBmY2NjZDRmNWUwZDFlOGY4ZjYwZDdlNzRhNTEyOTI4NzQ5Nzk1N2Y4NjU2YzUyOC5wbmc" alt="gundam, amoled wallpaper" title="gundam, amoled wallpaper">
		<div class="desc">
							&quot;gundam, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="4e90c73e38e365b9a176e9768dd631b34f22272ac5d18ab39ea4cbb6615f6c47">
	<div class="top">
		<img loading="lazy" src="/dynimg/-esfFiTgIJbPvtXJ_o5JiqCQr1KXtwC7fu-zzI6wBVc/w:400/Y29udGVudC9pbWFnZXMvNGU5MGM3M2UzOGUzNjViOWExNzZlOTc2OGRkNjMxYjM0ZjIyMjcyYWM1ZDE4YWIzOWVhNGNiYjY2MTVmNmM0Ny5wbmc" alt="Dragon made of fire, AMOLED wallpaper" title="Dragon made of fire, AMOLED wallpaper">
		<div class="desc">
							&quot;Dragon made of fire, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="1a65ad7e5306ac2848e6a9cf1d8db052547572b9cbea5681251e59e3f7d4b280">
	<div class="top">
		<img loading="lazy" src="/dynimg/PxCjWJS3YpB_wYwzxaIcYgg-zp0j61QBQjaVAEIzgS4/w:400/Y29udGVudC9pbWFnZXMvMWE2NWFkN2U1MzA2YWMyODQ4ZTZhOWNmMWQ4ZGIwNTI1NDc1NzJiOWNiZWE1NjgxMjUxZTU5ZTNmN2Q0YjI4MC5wbmc" alt="Golden retriever, AMOLED wallpaper, digital art" title="Golden retriever, AMOLED wallpaper, digital art">
		<div class="desc">
							&quot;Golden retriever, <b>AMOLED wallpaper</b>, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="5ad04979c803eb94a1658880a41768ebf4fa2f29705aef04ddf2adbb24f0819a">
	<div class="top">
		<img loading="lazy" src="/dynimg/F75nIPjQ8aLMQFGBhV-uC2acYoLhYfvbotqFBXs7rXU/w:400/Y29udGVudC9pbWFnZXMvNWFkMDQ5NzljODAzZWI5NGExNjU4ODgwYTQxNzY4ZWJmNGZhMmYyOTcwNWFlZjA0ZGRmMmFkYmIyNGYwODE5YS5wbmc" alt="Dragon made of fire, AMOLED wallpaper, logo mascot" title="Dragon made of fire, AMOLED wallpaper, logo mascot">
		<div class="desc">
							&quot;Dragon made of fire, <b>AMOLED wallpaper</b>, logo mascot&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="1fd3ceee2732dc3897c12186149f7ef419aa252aa4b9bcf16d07df837c93801d">
	<div class="top">
		<img loading="lazy" src="/dynimg/wS3YTGe1JaV81wg_lGzm6C49FnOlHM6ep-bmW7c0HO8/w:400/Y29udGVudC9pbWFnZXMvMWZkM2NlZWUyNzMyZGMzODk3YzEyMTg2MTQ5ZjdlZjQxOWFhMjUyYWE0YjliY2YxNmQwN2RmODM3YzkzODAxZC5wbmc" alt="Monsters, AMOLED wallpaper, digital art" title="Monsters, AMOLED wallpaper, digital art">
		<div class="desc">
							&quot;Monsters, <b>AMOLED wallpaper</b>, digital art&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="9f6c09e43b238b0a617f0d8615fdd7f178c0c0924c599768b67e022a033d24de">
	<div class="top">
		<img loading="lazy" src="/dynimg/IsSIfZgn633qBQJZjub40U_ALybuY3t1tkYFaTnVo3k/w:400/Y29udGVudC9pbWFnZXMvOWY2YzA5ZTQzYjIzOGIwYTYxN2YwZDg2MTVmZGQ3ZjE3OGMwYzA5MjRjNTk5NzY4YjY3ZTAyMmEwMzNkMjRkZS5wbmc" alt="gundam vs voltron, amoled wallpaper" title="gundam vs voltron, amoled wallpaper">
		<div class="desc">
							&quot;gundam vs voltron, <b>AMOLED wallpaper</b>&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="aadc8ea6033f1290b4242adb613163dbd94e1c6ced2d16df1f53f034b7d7f78e">
	<div class="top">
		<img loading="lazy" src="/dynimg/7os7ToX02Bzh7dzbl_KfoEDgpa9gnzoVp0ZyvcDJ6-k/w:400/Y29udGVudC9pbWFnZXMvYWFkYzhlYTYwMzNmMTI5MGI0MjQyYWRiNjEzMTYzZGJkOTRlMWM2Y2VkMmQxNmRmMWY1M2YwMzRiN2Q3Zjc4ZS5wbmc" alt="gundam, amoled wallpaper, mystical" title="gundam, amoled wallpaper, mystical">
		<div class="desc">
							&quot;gundam, <b>AMOLED wallpaper</b>, mystical&quot;
					</div>
	</div>
	</div>
					<div class="image-item" data-image-id="1137754f1d754007d410fe33bec77aad24541b40f06d394ac2e9fae346791ace">
	<div class="top">
		<img loading="lazy" src="/dynimg/swVdHl1cDa-ywMVf6IUx_W6ZEBPkU2eZzX9LEmiCJyA/w:400/Y29udGVudC9pbWFnZXMvMTEzNzc1NGYxZDc1NDAwN2Q0MTBmZTMzYmVjNzdhYWQyNDU0MWI0MGYwNmQzOTRhYzJlOWZhZTM0Njc5MWFjZS5wbmc" alt="Dragon made of fire, AMOLED wallpaper, logo mascot" title="Dragon made of fire, AMOLED wallpaper, logo mascot">
		<div class="desc">
							&quot;Dragon made of fire, <b>AMOLED wallpaper</b>, logo mascot&quot;
					</div>
	</div>
	</div>	</div>
	<p class="scroll-list-end">End of results</p>


    '''
    

    alt_texts = extract_img_alt(html_content)
    
    # Print extracted alt texts
    print("\n\nAlt texts from img tags:\n")
    for text in alt_texts:
        #print(qt(first_word(text)) + ',' + qt(fmt1(text)))
        print("list.Add(new ImagePromptModel(" + qt(first_word(text)) + ',' + qt(fmt1(text)) + "));")

    exit()


    h3_texts, strong_texts = extract_from_html(html_content)
    
    # Print extracted contents
    print("Texts from H3 tags:")
    for text in h3_texts:
        print(text)
    
    print("\nTexts from Strong tags:")
    for text in strong_texts:
        print(text.replace("”", "\"").replace("“", "\""))

    print("\n\n")
    for i in range(0, len(strong_texts)):
        print("list.Add(new ImagePromptModel(\"" + fmt(h3_texts[i]) + "\"," + fmt(strong_texts[i]) + "));")
        

