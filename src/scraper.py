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


def get_link_selector_pair_from_file_ref(
    file_ref: str = "../resources/sources/headache.txt",
) -> Optional[DataFrame]:
    df = pd.read_csv(file_ref, index_col=False)

    if isinstance(df, DataFrame):
        # Strip white space from column data.
        df.columns = df.columns.str.strip()
        return df


def get_html_text_from_link_and_selector(link: str, selector: str) -> List[str]:
    html_main = BeautifulSoup(requests.get(link).text).select_one(selector)

    if html_main:
        return [html_text.get_text() for html_text in html_main.find_all(text=True)]

    return []


def get_html_text_from_data_frame(df: DataFrame):
    return [
        body_text
        for r_i in range(len(df))
        for body_text in get_html_text_from_link_and_selector(
            df.iloc[r_i, 1], df.iloc[r_i, 0]
        )
    ]


df = get_link_selector_pair_from_file_ref()

if isinstance(df, DataFrame):
   print(get_html_text_from_data_frame(df))
