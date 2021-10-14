from pandas.core.frame import DataFrame
from scraper import get_df_from_csv
import os


def given_file_ref_when_loaded_then_data_frame_is_returned():
    current_file_ref = os.path.abspath(os.path.dirname(__file__))
    file_ref = os.path.join(current_file_ref, "../resources/sources/headache.csv")

    assert isinstance(get_df_from_csv(file_ref), DataFrame) == True

def given_invalid_file_ref_when_loaded_then_none_is_returned():
    assert get_df_from_csv('') == None
