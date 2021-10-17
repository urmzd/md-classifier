from pandas.core.frame import DataFrame
from scraper import get_df_from_csv, get_html
from requests.exceptions import ConnectionError
import pytest
import os


def given_file_path_when_get_df_from_csv_data_frame_is_returned():
    current_file_ref = os.path.abspath(os.path.dirname(__file__))
    file_ref = os.path.join(current_file_ref, "../resources/sources/headache.csv")
    print(file_ref)

    assert isinstance(get_df_from_csv(file_ref), DataFrame) == True


def given_invalid_file_path_when_get_df_from_csv_then_none_is_returned():
    with pytest.raises(FileNotFoundError):
        get_df_from_csv("")


def given_invalid_selector_when_get_html_then():
    with pytest.raises(ValueError):
        link = "https://google.com"
        selector = "#urmzd"
        get_html(link, selector)


def given_invalid_link_when_get_html_then():
    with pytest.raises(ConnectionError):
        link = "https://urmzd.com/urmzd"
        selector = "div"
        get_html(link, selector)
