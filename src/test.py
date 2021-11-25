#!/usr/bin/env python
import asyncio
from pyppeteer import launch
from typing import Optional

async def download_html(url: str, selector: str) -> Optional[str]:
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url, waitUntil="load")
    content = await page.querySelector(selector)

    html = None
    if content:
        html = await page.evaluate('(element) => element.textContent', content)
        print(html)

    await browser.close()
    return html

asyncio.run(
    download_html(
        "https://www.uptodate.com/contents/depression-the-basics?search=Patient%20education&source=search_result&selectedTitle=15~150&usage_type=default&display_rank=15", 
        "#topicText"
    )
)
