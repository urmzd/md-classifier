from typing import List, Optional
from re import search
from requests import get

def get_links_by_file_ref(file_ref: str = "../resources/sources/headache.txt") -> List[str]:
    with open(file_ref, "r") as source_file:
        return [link_ref for link_ref in source_file]

def get_html_by_link_ref(link_ref: str) -> Optional[str]:
    response = get(link_ref)

    if response.status_code == 200:
        return response.text

def get_body_from_html(html: str) -> Optional[str]:
    body_regex = r"<body>(.*?)<\/body>"
    matches = search(html, body_regex)

    if matches:
        return matches.group(0)







