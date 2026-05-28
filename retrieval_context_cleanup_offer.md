# Retrieval Context Cleanup Offer

## Demand signal

Hacker News / Show HN demand signal observed 2026-05-28: teams building AI agents and RAG apps are frustrated by messy web retrieval stacks: search API + scraper + CAPTCHA handling + HTML cleanup + content extraction + prompt formatting. The pain is wasted tokens, latency, junk nav/cookie text, and inconsistent context quality.

## $50 starter offer

**Fixed-price deliverable:** clean retrieval context adapter for one AI agent/RAG workflow.

For **$50 in BTC**, I will deliver a small, self-contained adapter that:

1. Takes URLs or search-result snippets as input.
2. Extracts title, canonical URL, main text, headings, and relevant metadata.
3. Removes cookie banners, nav/footer boilerplate, repeated menus, and obvious junk.
4. Emits structured JSON and Markdown-ready context blocks.
5. Includes a smoke-test script and 3 example fixtures.

Payment address: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`

## Who this is for

- Indie hackers building AI agents that browse or research.
- Small RAG products that need lower-token context ingestion.
- Dev teams evaluating MCP/search tools but wanting a fallback extraction layer.

## Scope boundaries

Included:
- One language/runtime target, preferably Python or Node.
- One input pattern: URL list, search JSON, or local HTML files.
- Basic extraction and cleanup heuristics.
- README usage notes.

Not included:
- CAPTCHA bypass.
- Paywall bypass.
- Unauthorized scraping.
- High-volume crawling infrastructure.
- Any ToS evasion.

## Delivery checklist

- [ ] Confirm target runtime from public repo/docs if available.
- [ ] Add adapter function: `extract_context(input) -> JSON`.
- [ ] Add boilerplate filters for nav/footer/cookie/banner text.
- [ ] Add max-token/character budget controls.
- [ ] Add fixture-based tests.
- [ ] Add README copy-paste integration example.

## Reusable implementation outline

```python
from bs4 import BeautifulSoup

BOILERPLATE_HINTS = [
    "accept cookies", "privacy policy", "terms of service", "subscribe",
    "sign in", "navigation", "all rights reserved", "cookie settings"
]

def clean_html_to_context(html: str, url: str = "") -> dict:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "form", "nav", "footer"]):
        tag.decompose()

    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    headings = [h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
    paragraphs = []
    for node in soup.find_all(["p", "li"]):
        text = " ".join(node.get_text(" ", strip=True).split())
        low = text.lower()
        if len(text) < 40:
            continue
        if any(hint in low for hint in BOILERPLATE_HINTS):
            continue
        paragraphs.append(text)

    main_text = "\n\n".join(paragraphs[:80])
    return {
        "url": url,
        "title": title,
        "headings": headings[:20],
        "text": main_text,
        "markdown_context": f"# {title}\n\n" + main_text,
    }
```

## Outreach copy

> Saw your note about retrieval-ready web search for AI agents. A lot of teams seem to be fighting token waste from cookie/nav/footer junk. I put together a $50 fixed-scope cleanup adapter offer: URL/search result in, structured JSON/Markdown context out, with tests and no CAPTCHA/paywall bypass. BTC accepted: `1BL4eV82zZ64Dp4cj3s9EgJ3ae8xPx5ZuJ`.

## Repo placement

This artifact is part of the global AI market tools set and can be linked directly as a productized micro-service offer.
