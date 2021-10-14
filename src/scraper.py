#!/usr/bin/env python
# Create types.
from typing import Optional, Tuple, List
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import requests
import pandas as pd

Link = str
Selector = str
LinkSelectorPair = Tuple[Link, Selector]


def get_df_from_csv(
    file_ref: str = "../resources/sources/headache.csv",
) -> Optional[DataFrame]:
    df = pd.read_csv(file_ref)

    if isinstance(df, DataFrame):
        # Strip white space from column data.
        print(df)
        df.columns = df.columns.str.strip()
        return df

    return None


def get_html(link: str, selector: str) -> List[str]:
    html_main = BeautifulSoup(
        requests.get(link).text, features="html.parser"
    ).select_one(selector)

    if html_main:
        return [html_text.get_text() for html_text in html_main.find_all(text=True)]

    return []


def get_html_from_df(df: Optional[DataFrame]):
    if df is not None:
        return [
            body_text
            for r_i in range(len(df))
            for body_text in get_html(df.iloc[r_i, 1], df.iloc[r_i, 0])
        ]
    return []


def split_words_by_whitespace(texts: List[str]):
    return [subtext for text in texts for subtext in text.split(" ")]


def create_csv_string(texts: List[str]) -> str:
    return ",".join(texts)


def output_text_to_file_ref(
    text: str, file_ref: str = "../resources/targets/headache.csv"
):
    with open(file_ref, "w") as target:
        target.write(text)


if __name__ == "__main__":
    df = get_df_from_csv()

    if df is not None:
        try:
            output_text_to_file_ref(
                create_csv_string(
                    split_words_by_whitespace(get_html_from_df(get_df_from_csv()))
                )
            )
            print("Parsing successful.")
        except:
            print("Parsing failed.")
