"""Validate generated Jekyll output without third-party dependencies."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from xml.etree import ElementTree

root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
origin = "https://paraita-io.github.io"
base = "/horo-website/"
errors = []


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.ids = set()
        self.h1 = 0
        self.json_blocks = []
        self.json_text = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if "id" in a:
            if a["id"] in self.ids:
                errors.append(f"Duplicate ID: {a['id']}")
            self.ids.add(a["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "script" and a.get("type") == "application/ld+json":
            self.json_text = ""

    def handle_data(self, data):
        if self.json_text is not None:
            self.json_text += data

    def handle_endtag(self, tag):
        if tag == "script" and self.json_text is not None:
            self.json_blocks.append(json.loads(self.json_text))
            self.json_text = None


pages = {}
for path in root.glob("*.html"):
    text = path.read_text()
    assert "{{" not in text and "{%" not in text, f"Unrendered Liquid in {path}"
    pages[path.name] = Page(text)

assert len(pages) == 14, f"Expected 14 localized pages, got {len(pages)}"
for name, page in pages.items():
    assert page.h1 == 1, f"{name}: expected one H1"
    canonical = [a["href"] for t, a in page.tags if t == "link" and a.get("rel") == "canonical"]
    expected = origin + base + ("" if name == "index.html" else name)
    assert canonical == [expected], f"{name}: incorrect canonical {canonical}"
    alts = {a["hreflang"]: a["href"] for t, a in page.tags if t == "link" and a.get("rel") == "alternate"}
    assert set(alts) == {"en", "fr", "x-default"}, name
    for tag, attrs in page.tags:
        target = attrs.get("href") if tag in ("a", "link") else attrs.get("src")
        if target is None:
            continue
        assert target not in ("", "#"), f"{name}: empty destination"
        url = urlparse(urljoin(expected, target))
        if url.netloc != urlparse(origin).netloc or url.scheme not in ("http", "https"):
            continue
        assert url.path.startswith(base), f"{name}: URL outside site: {target}"
        relative = unquote(url.path[len(base):]) or "index.html"
        file = root / relative
        assert file.exists(), f"{name}: missing {relative}"
        if url.fragment and file.suffix == ".html":
            assert unquote(url.fragment) in pages[file.name].ids, f"{name}: missing anchor {target}"
    peer_name = name.replace("-fr.html", ".html") if name.endswith("-fr.html") else name.replace(".html", "-fr.html")
    peer_alts = {a["hreflang"]: a["href"] for t, a in pages[peer_name].tags if t == "link" and a.get("rel") == "alternate"}
    assert alts == peer_alts, f"{name}: language links are not reciprocal"

for name in ["index.html", "index-fr.html", "plans.html", "plans-fr.html", "get-started.html", "get-started-fr.html"]:
    assert any(a.get("href") == "https://apps.apple.com/app/horo-coach/id6756943315" for _, a in pages[name].tags), name
for name in ["index.html", "index-fr.html"]:
    assert pages[name].json_blocks[0]["@type"] == "SoftwareApplication"

xml = ElementTree.parse(root / "sitemap.xml")
urls = [e.text for e in xml.findall(".//{*}loc")]
assert len(urls) == len(set(urls)) == len(pages), "Incomplete or duplicate sitemap"
assert set(urls) == {origin + base + ("" if name == "index.html" else name) for name in pages}
assert not errors, errors
print(f"PASS: {len(pages)} pages; local links, anchors, App Store CTAs, canonical URLs, reciprocal languages, JSON-LD and sitemap.")
