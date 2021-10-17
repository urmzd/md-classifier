from typing import List


def split_words_by_whitespace(texts: List[str]):
    return [subtext for text in texts for subtext in text.split(" ")]


def create_csv_string(texts: List[str]) -> str:
    return ",".join(texts)


def output_text_to_file_ref(
    text: str, file_ref: str = "../resources/targets/headache.csv"
):
    with open(file_ref, "w") as target:
        target.write(text)
