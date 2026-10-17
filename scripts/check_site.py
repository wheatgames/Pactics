"""Check generated pages and local links without network requests."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.h1_count = 0
        self.feed(html)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        if tag == "h1":
            self.h1_count += 1
        for attribute in ("href", "src"):
            if attributes.get(attribute):
                self.links.append(attributes[attribute])


def check_site(directory, baseurl):
    root = directory.resolve()
    prefix = baseurl.rstrip("/")
    errors = []
    required = ("index.html", "privacy.html", "terms.html", "delete-account.html", "support.html", "404.html")
    pages = {path: Page(path.read_text(encoding="utf-8")) for path in root.rglob("*.html")}
    for name in required:
        path = root / name
        if path not in pages:
            errors.append(f"Missing public page: {name}")
        elif pages[path].h1_count != 1:
            errors.append(f"{name}: expected a single main heading")
    for old_directory in ("AnimalAlphabet", "GiftExchanger", "jekyll"):
        if (root / old_directory).exists():
            errors.append(f"Unrelated template pages are still published: {old_directory}")
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        current_url = prefix + "/" + relative
        for link in page.links:
            parsed = urlsplit(urljoin(current_url, link))
            if parsed.scheme or parsed.netloc:
                continue
            url_path = unquote(parsed.path)
            if prefix and not url_path.startswith(prefix + "/"):
                errors.append(f"{relative}: link escapes the site's path: {link}")
                continue
            target = (root / url_path[len(prefix):].lstrip("/")).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{relative}: link escapes the output directory: {link}")
                continue
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{relative}: missing target: {link}")
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f"{relative}: missing section: {link}")
    return errors, len(pages)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--baseurl", default="/Pactics")
    arguments = parser.parse_args()
    problems, count = check_site(arguments.directory, arguments.baseurl)
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        raise SystemExit(1)
    print(f"PASS: {count} pages checked; all local links, section anchors and assets resolve.")
