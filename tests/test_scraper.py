import pandas as pd
from pandas.core.frame import DataFrame
from scraper import get_df_from_csv, get_html, get_html_from_df
from requests.exceptions import ConnectionError
import pytest
import os


def given_valid_file_path_when_get_df_from_csv_data_frame_is_returned():
    current_file_ref = os.path.abspath(os.path.dirname(__file__))
    file_ref = os.path.join(current_file_ref, "../resources/sources/headache.csv")
    print(file_ref)

    assert isinstance(get_df_from_csv(file_ref), DataFrame) == True


def given_invalid_file_path_when_get_df_from_csv_then_none_is_returned():
    with pytest.raises(FileNotFoundError):
        get_df_from_csv("")


def given_invalid_selector_when_get_html_then_raise_value_error():
    with pytest.raises(ValueError):
        link = "https://google.com"
        selector = "#urmzd"
        get_html(link, selector)


def given_invalid_link_when_get_html_then_raise_value_error():
    with pytest.raises(ConnectionError):
        link = "https://urmzd.com/urmzd"
        selector = "div"
        get_html(link, selector)


def given_valid_data_frame_when_get_html_from_df_then_list_of_str_is_returned():
    data = {
        "selector": ["div", "div"],
        "link": ["https://google.com", "https://youtube.com"],
    }
    df = pd.DataFrame(data=data)

    assert (len(get_html_from_df(df)) > 0) == True


def given_invalid_data_frame_when_get_html_from_df_then_raise_value_error():
    data = {
        "selector": ["#urmzd", "#urmzd"],
        "link": ["https://google.com", "https://youtube.com"],
    }
    df = pd.DataFrame(data=data)

    with pytest.raises(ValueError):
        get_html_from_df(df)
