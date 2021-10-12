from typing import List

def get_links_by_file_ref(file_ref:str="../resources/sources/headache.txt") -> List[str]:
    with open(file_ref, "r") as source_file:
        return [link_ref for link_ref in source_file]




