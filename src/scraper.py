#!/usr/bin/env python
from typing import List
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import requests
import pandas as pd

# Type definitions.
Selector = str
Link = str
FilePath = str

def get_df_from_csv(
    file_path: FilePath = "../resources/sources/headache.csv",
) -> DataFrame:
    df = pd.read_csv(file_path)

    if isinstance(df, DataFrame):
        df.columns = df.columns.str.strip()
        return df

    raise ValueError("The dataframe produced unexpected type.")


def get_html(link: Link, selector: Selector) -> List[str]:
    html_raw = requests.get(link)
    html_content = html_raw.text
    html_full = BeautifulSoup(html_content, features="html.parser")
    html_selection = html_full.select_one(selector)

    if not html_selection:
        raise ValueError(
            "The selector provided was unable to match anything from the link provided."
        )

    html_selection_texts = html_selection.find_all(text=True)

    return [html_text.get_text() for html_text in html_selection_texts]


def get_html_from_df(df: DataFrame):
    return [
        body_text
        for r_i in range(len(df))
        for body_text in get_html(df.iloc[r_i, 1], df.iloc[r_i, 0])
    ]




if __name__ == "__main__":
    try:
        output_text_to_file_ref(
            create_csv_string(
                split_words_by_whitespace(get_html_from_df(get_df_from_csv()))
            )
        )
        print("Parsing successful.")
    except:
        print("Parsing failed.")
