"""
Crawl tmasolutions.com/insights -> articles-database.json
Chay: python crawl_insights.py
Nen chay dinh ky (hang tuan/thang) de cap nhat bai moi.
"""

import json, re, sys, time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

BASE = 'https://www.tmasolutions.com'
OUTPUT = 'articles-database.json'

CARD_SEL   = '[class*=case_study]:not([class*=image]):not([class*=content]):not([class*=wrap])'
TITLE_SEL  = 'a[href*="/insights/"]:not([class*=image])'
TAG_SEL    = '[class*=tag], [class*=category], [class*=label]'
PAGE_SEL   = '[class*=pagination] .item:not(.first):not(.last):not(.prev):not(.next):not(.is_disabled)'

def extract_page(page):
    """Extract all article cards from current page."""
    cards = page.eval_on_selector_all(
        '[class*=case_study]:not([class*=_image]):not([class*=_content])',
        """els => els
          .filter(e => e.querySelectorAll('a[href*="/insights/"]').length > 0)
          .map(e => {
            const link = e.querySelector('a[href*="/insights/"]:not([class*=image])') || e.querySelector('a[href*="/insights/"]');
            const title = link ? (link.title || link.innerText.trim()) : '';
            const href  = link ? link.href : '';
            const allText = e.innerText.trim();
            // Tags: lines before the description (usually 1-2 short lines after title)
            const lines = allText.split('\\n').map(l => l.trim()).filter(Boolean);
            // Description: longest line that's not the title and not a short tag
            const desc = lines.filter(l => l.length > 60 && l !== title && !l.startsWith('http')).slice(0,1)[0] || '';
            const tags = lines.filter(l => l.length > 0 && l.length < 40 && l !== title).slice(0,4);
            return { title, href, tags, desc };
          })
          .filter(c => c.href && c.title)
        """
    )
    return cards

def run():
    articles = []
    seen = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={'width': 1280, 'height': 900})
        page = ctx.new_page()

        print('Fetching page 1...')
        page.goto(f'{BASE}/insights', wait_until='networkidle', timeout=30000)

        # How many pages?
        page_items = page.locator(PAGE_SEL).all()
        page_nums  = []
        for item in page_items:
            txt = item.inner_text().strip()
            if txt.isdigit():
                page_nums.append(int(txt))
        total_pages = max(page_nums) if page_nums else 1
        print(f'Total pages: {total_pages}')

        for pg in range(1, total_pages + 1):
            if pg > 1:
                print(f'Navigating to page {pg}...')
                # Click the page number item
                target = page.locator(f'[class*=pagination] .item').filter(has_text=str(pg))
                target.first.click()
                page.wait_for_load_state('networkidle')
                time.sleep(1)

            cards = extract_page(page)
            print(f'  Page {pg}: {len(cards)} cards found')
            for c in cards:
                if c['href'] not in seen:
                    seen.add(c['href'])
                    # Normalize slug-based keywords from URL
                    slug = c['href'].split('/insights/')[-1].rstrip('/')
                    slug_words = [w for w in re.split(r'[-_]', slug) if len(w) > 3]
                    articles.append({
                        'title':      c['title'],
                        'url':        c['href'],
                        'topic_tags': c['tags'],
                        'slug_keywords': slug_words[:10],
                        'summary':    c['desc']
                    })

        browser.close()

    print(f'\nTotal articles: {len(articles)}')
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f'Saved to {OUTPUT}')
    # Preview first 3
    for a in articles[:3]:
        print(f'\n  Title: {a["title"]}')
        print(f'  URL:   {a["url"]}')
        print(f'  Tags:  {a["topic_tags"]}')
        print(f'  Slug:  {a["slug_keywords"]}')
        print(f'  Desc:  {a["summary"][:100]}')

if __name__ == '__main__':
    run()
