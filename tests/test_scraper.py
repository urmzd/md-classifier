from pandas.core.frame import DataFrame
from scraper import get_df_from_csv
import pytest
import os


def given_file_path_when_loaded_then_data_frame_is_returned():
    current_file_ref = os.path.abspath(os.path.dirname(__file__))
    file_ref = os.path.join(current_file_ref, "../resources/sources/headache.csv")
    print(file_ref)

    assert isinstance(get_df_from_csv(file_ref), DataFrame) == True


def given_invalid_file_path_when_loaded_then_none_is_returned():
    with pytest.raises(FileNotFoundError):

        get_df_from_csv("")
