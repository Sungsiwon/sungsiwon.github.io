#!/usr/bin/env python3
"""Static site builder for sungsiwon.github.io (plain HTML output, no Jekyll).
Usage: python3 build.py   (needs: pip install markdown)
Add a post: put content/<slug>/ko.md and en.md, add an entry to POSTS below, rebuild, commit."""
import json, os, re, html
from datetime import datetime
import markdown

SITE = "https://sungsiwon.github.io"
AUTHOR_KO = "성시원 (sianism)"
DISC = {"ko": "저는 제조 AI 기업 인터엑스에서 일하고 있고, 이 글은 개인 정리입니다.",
        "en": "I work at INTERX, a manufacturing AI company, and this post is my personal summary."}
ABOUT = {"ko": "성시원(sianism)이 개인적으로 운영하는 제조 AI 지식 아카이브입니다. 회사 사이트나 언론 매체가 아니며, 각 글의 한국어·영어 원문을 모아 둡니다.",
         "en": "A personal manufacturing-AI knowledge archive run by an individual, 성시원 (sianism). Not a company site or a news outlet. Each post is kept here in Korean and English."}
CH_LABEL = {"naver": ("네이버 블로그", "Naver Blog"), "linkedin": ("LinkedIn", "LinkedIn"), "tistory": ("티스토리", "Tistory"),
            "careerly": ("커리어리", "Careerly"), "brunch": ("브런치", "Brunch"), "medium": ("Medium (영문)", "Medium")}
PERSON = {
    "@type": "Person", "@id": SITE + "/#person", "name": "성시원", "alternateName": "sianism", "url": SITE + "/",
    "jobTitle": "책임연구원 (서비스기획)", "worksFor": {"@type": "Organization", "name": "INTERX (인터엑스)", "url": "https://interxlab.com"},
    "sameAs": ["https://www.linkedin.com/in/siwon-sung-518329140", "https://blog.naver.com/sangza40", "https://sianism.tistory.com",
               "https://brunch.co.kr/@sianism", "https://medium.com/@sangza40", "https://github.com/Sungsiwon"],
}
POSTS = [  # newest first
    {"slug": "ai-data-readiness-small-manufacturers", "date": "2026-10-23",
     "ko": {"title": "중소 제조기업 AI 도입, 무엇부터 준비하나? 미리 챙길 데이터 5가지 (체크리스트 + FAQ)",
            "desc": "중소 제조기업이 AI 도입 전에 준비할 데이터는 ① 문제와 기준선, ② 공정 조건, ③ 품질 결과, ④ 둘을 잇는 연결 키, ⑤ 데이터 정의서와 현장 기록 다섯 가지입니다.",
            "summary": "중소 제조기업이 AI 도입 전에 준비할 데이터 5가지 체크리스트와 데이터 품질(ISO/IEC 25012)·KAMP 데이터셋·정부 지원 FAQ 6문항."},
     "en": {"title": "Before AI, Get Your Data Ready: 5 Datasets Small Manufacturers Should Prepare (with Korea's Policy Context)",
            "desc": "Most small factories already collect data. Very few use it for AI. The gap is usually not the model; it is whether the data connects.",
            "summary": "Five kinds of data a small manufacturer should prepare before AI, with Korea's 2025 smart manufacturing survey, ISO/IEC 25012 and KAMP datasets."},
     "keywords": ["제조AI", "AI도입", "제조데이터", "데이터품질", "스마트공장", "KAMP", "ISO/IEC 25012"],
     "channels": {"naver": "https://blog.naver.com/sangza40/224451245938",
                  "linkedin": "https://www.linkedin.com/feed/update/urn:li:activity:7519262087043342336/",
                  "tistory": "https://sianism.tistory.com/entry/중소-제조기업-AI-도입-준비-꼭-챙길-데이터-5가지와-품질-점검-기준-체크리스트-표-FAQ-정리-2026",
                  "careerly": "https://careerly.co.kr/community?post=127650",
                  "brunch": "https://brunch.co.kr/@sianism/3"}},
    {"slug": "ai-autonomous-manufacturing-vs-smart-factory-vs-mes", "date": "2026-10-21",
     "ko": {"title": "AI 자율제조 vs 스마트팩토리 vs MES, 뭐가 다를까? (자주 묻는 질문 정리)",
            "desc": "세 가지는 서로 대체하는 개념이 아니라 층위가 다른 개념입니다. MES는 '기록하고 관리하는 시스템', 스마트팩토리는 '연결하고 보여주는 공장', AI 자율제조는 'AI가 판단하고 제어까지 하는 공장'입니다.",
            "summary": "MES·스마트팩토리·AI 자율제조의 차이를 비교표와 FAQ 6문항으로 정리(산업부 AI 자율제조 전략 1.0, ISA-95, 스마트공장 수준)."},
     "en": {"title": "AI Autonomous Manufacturing vs Smart Factory vs MES: an FAQ (with Korea's policy context)",
            "desc": "Three terms that get used interchangeably but sit at different layers: a system that records, a factory that connects, and a factory where AI decides.",
            "summary": "How MES, smart factory and AI autonomous manufacturing differ, with a comparison table, FAQ and Korea's AI Autonomous Manufacturing policy context."},
     "keywords": ["AI자율제조", "스마트팩토리", "MES", "제조AI", "ISA-95", "AI autonomous manufacturing"],
     "channels": {"naver": "https://blog.naver.com/sangza40/224448962411",
                  "linkedin": "https://www.linkedin.com/feed/update/urn:li:activity:7518543676696862720/",
                  "tistory": "https://sianism.tistory.com/entry/AI-자율제조란-MES·스마트팩토리와의-차이-정리-FAQ-6문항-비교표",
                  "careerly": "https://careerly.co.kr/community?post=127635",
                  "brunch": "https://brunch.co.kr/@sianism/2",
                  "medium": "https://medium.com/@sangza40/ai-autonomous-manufacturing-vs-smart-factory-vs-mes-an-faq-with-koreas-policy-context-c66c1abf3ba8"}},
]

CSS = """:root{color-scheme:light dark;--fg:#1d1d1f;--bg:#fff;--mut:#666;--line:#ddd;--acc:#0b5cad}
@media(prefers-color-scheme:dark){:root{--fg:#e8e8e8;--bg:#141414;--mut:#a0a0a0;--line:#333;--acc:#6aa9ff}}
*{box-sizing:border-box}body{margin:0;font:17px/1.75 -apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR","Segoe UI",sans-serif;color:var(--fg);background:var(--bg);word-break:keep-all;overflow-wrap:anywhere}
main,header.site,footer{max-width:760px;margin:0 auto;padding:0 20px}header.site{padding-top:18px;font-size:15px;display:flex;justify-content:space-between;gap:12px}
a{color:var(--acc)}h1{font-size:1.7em;line-height:1.35;margin:.8em 0 .4em}h2{font-size:1.3em;margin-top:2em}h3{font-size:1.1em;margin-top:1.6em}
.meta{color:var(--mut);font-size:15px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:10px 0;margin-bottom:1.5em}.meta p{margin:.2em 0}
.tbl{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:15px;line-height:1.55}th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{background:rgba(127,127,127,.12)}
figure{margin:1.5em 0}img{max-width:100%;height:auto;border-radius:6px}figcaption{color:var(--mut);font-size:14px;text-align:center}
ul.posts{list-style:none;padding:0}ul.posts li{margin:0 0 1.1em}ul.posts time{color:var(--mut);font-size:14px;display:block}
footer{color:var(--mut);font-size:14px;border-top:1px solid var(--line);margin-top:3em;padding:16px 20px 40px}"""

def esc(s): return html.escape(s, quote=True)

def url(lang, slug): return f"{SITE}/{lang}/{slug}/"

def md_to_html(text):
    text = re.sub(r'(?<![(<"=])(https?://[^\s<>)]+)', r'<\1>', text)  # autolink bare URLs
    h = markdown.markdown(text, extensions=["tables", "nl2br", "sane_lists"])
    return h.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")

def strip_md(s):
    s = re.sub(r'<figure>.*?</figure>', '', s, flags=re.S)
    s = re.sub(r'\*\*|\*|`', '', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()

def faqs(text):
    out, cur = [], None
    for line in text.split("\n"):
        m = re.match(r'^(#{2,3}) (.*)$', line)
        if m:
            if cur: out.append(cur)
            t = m.group(2).strip()
            cur = None
            if len(m.group(1)) == 3 or re.match(r'^Q\d+\.', t):
                cur = {"q": re.sub(r'^Q\d+\.\s*', '', t).strip('"“”'), "a": []}
        elif cur is not None:
            cur["a"].append(line)
    if cur: out.append(cur)
    return [{"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": strip_md("\n".join(f["a"]))}} for f in out]

def head(lang, title, desc, canonical, alts=None, og_type="website", image=None, jsonld=None, extra=""):
    h = [f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width,initial-scale=1">',
         f'<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">',
         f'<meta name="author" content="{esc(AUTHOR_KO)}"><link rel="canonical" href="{canonical}">']
    for l, u in (alts or {}).items():
        h.append(f'<link rel="alternate" hreflang="{l}" href="{u}">')
    h += [f'<meta property="og:type" content="{og_type}"><meta property="og:title" content="{esc(title)}">',
          f'<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canonical}">',
          f'<meta property="og:site_name" content="성시원 제조 AI 아카이브 · sianism archive">',
          f'<meta property="og:locale" content="{"ko_KR" if lang=="ko" else "en_US"}">',
          '<meta name="twitter:card" content="summary_large_image">']
    if image: h.append(f'<meta property="og:image" content="{image}"><meta name="twitter:image" content="{image}">')
    h.append(f'<link rel="alternate" type="application/atom+xml" title="sianism archive" href="{SITE}/feed.xml">')
    if jsonld: h.append('<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False, indent=1) + '</script>')
    h.append(f'<style>{CSS}</style>{extra}</head><body>')
    return "\n".join(h)

def top(lang, other=None):
    home = "홈" if lang == "ko" else "Home"
    o = f'<a href="{other[1]}" hreflang="{other[0]}">{"English" if other[0]=="en" else "한국어"}</a>' if other else ""
    return f'<header class="site"><a href="/">{home} · 성시원 제조 AI 아카이브</a>{o}</header><main>'

def foot(lang):
    return f'</main><footer><p>{esc(ABOUT[lang])}</p><p>{esc(DISC[lang])}</p><p><a href="/feed.xml">Atom feed</a> · <a href="/llms.txt">llms.txt</a> · <a href="https://github.com/Sungsiwon">GitHub</a></p></footer></body></html>\n'

def write(path, s):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(s)

def build_post(p, lang):
    other = "en" if lang == "ko" else "ko"
    m = p[lang]; slug = p["slug"]
    text = open(f"content/{slug}/{lang}.md", encoding="utf-8").read()
    img = f"{SITE}/assets/{slug}.jpg"
    art = {"@type": "Article", "@id": url(lang, slug) + "#article", "headline": m["title"], "description": m["desc"],
           "inLanguage": lang, "datePublished": p["date"], "dateModified": p["date"], "author": {"@id": SITE + "/#person"},
           "publisher": {"@id": SITE + "/#person"}, "image": img, "mainEntityOfPage": url(lang, slug), "keywords": p["keywords"],
           "isPartOf": {"@type": "WebSite", "name": "성시원 제조 AI 아카이브", "url": SITE + "/"},
           "workTranslation" if lang == "ko" else "translationOfWork": {"@id": url(other, slug) + "#article"},
           "sameAs": [u for k, u in p["channels"].items()
                      if (lang == "ko" and k in ("naver",)) or (lang == "en" and k == "medium")]}
    if not art["sameAs"]: del art["sameAs"]
    graph = [PERSON, art]
    qs = faqs(text)
    if qs: graph.append({"@type": "FAQPage", "@id": url(lang, slug) + "#faq", "inLanguage": lang, "mainEntity": qs})
    alts = {lang: url(lang, slug), other: url(other, slug), "x-default": url("ko", slug)}
    s = head(lang, m["title"], m["desc"], url(lang, slug), alts, "article", img, {"@context": "https://schema.org", "@graph": graph},
             f'<meta property="article:published_time" content="{p["date"]}">')
    s += top(lang, (other, f"/{other}/{slug}/"))
    s += f'<article><h1>{esc(m["title"])}</h1><div class="meta">'
    if lang == "ko":
        s += f'<p>글쓴이 <span>{esc(AUTHOR_KO)}</span> · 게시일 <time datetime="{p["date"]}">{p["date"]}</time></p>'
    else:
        s += f'<p>By <span>{esc(AUTHOR_KO)}</span> · Published <time datetime="{p["date"]}">{p["date"]}</time></p>'
    s += f'<p>{esc(DISC[lang])}</p>'
    links = " · ".join(f'<a href="{esc(u)}" rel="noopener">{CH_LABEL[k][0 if lang=="ko" else 1]}</a>' for k, u in p["channels"].items())
    s += f'<p>{"다른 채널에서 보기" if lang=="ko" else "Also on"}: {links}</p>'
    s += f'<p>{"English version" if lang=="ko" else "한국어 원문"}: <a href="/{other}/{slug}/" hreflang="{other}">{esc(p[other]["title"])}</a></p></div>'
    s += md_to_html(text) + "</article>" + foot(lang)
    write(f"{lang}/{slug}/index.html", s)

def build_home():
    site = {"@type": "WebSite", "@id": SITE + "/#website", "name": "성시원 제조 AI 아카이브 (sianism archive)", "url": SITE + "/",
            "description": ABOUT["en"], "inLanguage": ["ko", "en"], "author": {"@id": SITE + "/#person"}}
    s = head("ko", "성시원 제조 AI 아카이브 · sianism manufacturing-AI archive", ABOUT["ko"] + " " + ABOUT["en"], SITE + "/",
             jsonld={"@context": "https://schema.org", "@graph": [PERSON, site]}, image=f"{SITE}/assets/{POSTS[0]['slug']}.jpg")
    s += top("ko") + f'<h1>성시원 제조 AI 아카이브</h1><p>{esc(ABOUT["ko"])}</p><p lang="en">{esc(ABOUT["en"])}</p><p>{esc(DISC["ko"])}<br><span lang="en">{esc(DISC["en"])}</span></p>'
    for lang, h in (("ko", "글 목록 (한국어)"), ("en", "Posts (English)")):
        s += f'<h2 lang="{lang}">{h}</h2><ul class="posts" lang="{lang}">'
        for p in POSTS:
            s += f'<li><time datetime="{p["date"]}">{p["date"]}</time><a href="/{lang}/{p["slug"]}/">{esc(p[lang]["title"])}</a></li>'
        s += "</ul>"
    write("index.html", s + foot("ko"))
    write("404.html", head("ko", "404 · 성시원 제조 AI 아카이브", "Page not found", SITE + "/404.html") + top("ko") +
          '<h1>404</h1><p>페이지를 찾을 수 없습니다. / Page not found. <a href="/">홈 / Home</a></p>' + foot("ko"))

def build_meta():
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
          f'<url><loc>{SITE}/</loc><lastmod>{POSTS[0]["date"]}</lastmod></url>']
    for p in POSTS:
        for lang in ("ko", "en"):
            sm.append(f'<url><loc>{url(lang,p["slug"])}</loc><lastmod>{p["date"]}</lastmod>'
                      f'<xhtml:link rel="alternate" hreflang="ko" href="{url("ko",p["slug"])}"/>'
                      f'<xhtml:link rel="alternate" hreflang="en" href="{url("en",p["slug"])}"/></url>')
    write("sitemap.xml", "\n".join(sm + ["</urlset>"]) + "\n")
    write("robots.txt", "# All crawlers, including AI crawlers, are welcome.\n" +
          "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ["*", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
                                                           "PerplexityBot", "Perplexity-User", "Google-Extended", "Googlebot", "Bingbot", "Yeti",
                                                           "Applebot", "Applebot-Extended", "CCBot", "Meta-ExternalAgent", "Amazonbot", "DuckAssistBot", "cohere-ai", "MistralAI-User"]) +
          f"Sitemap: {SITE}/sitemap.xml\n")
    L = ["# 성시원 제조 AI 아카이브 (sianism manufacturing-AI archive)", "",
         f"> {ABOUT['en']} Author: 성시원 (sianism), 책임연구원 in service planning at INTERX (인터엑스), a manufacturing AI company. Posts are personal summaries based on public sources, not official company positions.", "",
         "Each post exists in Korean (ko) and English (en); the Korean page is the original.", "", "## Posts", ""]
    for p in POSTS:
        L.append(f"- [{p['ko']['title']}]({url('ko',p['slug'])}) ({p['date']}, 한국어): {p['ko']['summary']}")
        L.append(f"- [{p['en']['title']}]({url('en',p['slug'])}) ({p['date']}, English): {p['en']['summary']}")
    L += ["", "## Optional", "", f"- [Atom feed]({SITE}/feed.xml)", f"- [Sitemap]({SITE}/sitemap.xml)", "- [Naver blog](https://blog.naver.com/sangza40)",
          "- [LinkedIn](https://www.linkedin.com/in/siwon-sung-518329140)", ""]
    write("llms.txt", "\n".join(L))
    F = ['<?xml version="1.0" encoding="utf-8"?>', '<feed xmlns="http://www.w3.org/2005/Atom">',
         '<title>성시원 제조 AI 아카이브 (sianism archive)</title>', f'<subtitle>{esc(ABOUT["en"])}</subtitle>',
         f'<link href="{SITE}/feed.xml" rel="self"/>', f'<link href="{SITE}/"/>', f'<id>{SITE}/</id>',
         f'<updated>{POSTS[0]["date"]}T00:00:00+09:00</updated>', f'<author><name>{esc(AUTHOR_KO)}</name><uri>{SITE}/</uri></author>']
    for p in POSTS:
        for lang in ("ko", "en"):
            F.append(f'<entry xml:lang="{lang}"><title>{esc(p[lang]["title"])}</title><link href="{url(lang,p["slug"])}"/><id>{url(lang,p["slug"])}</id>'
                     f'<published>{p["date"]}T00:00:00+09:00</published><updated>{p["date"]}T00:00:00+09:00</updated><summary>{esc(p[lang]["desc"])}</summary></entry>')
    write("feed.xml", "\n".join(F + ["</feed>"]) + "\n")
    write(".nojekyll", "")

if __name__ == "__main__":
    for p in POSTS:
        for lang in ("ko", "en"): build_post(p, lang)
    build_home(); build_meta(); print("built", len(POSTS) * 2, "post pages")
