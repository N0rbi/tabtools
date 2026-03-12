import datetime

import pandas as pd
import pandas.testing as pdt
import pytest

from tabtool.models import BriefSummary, FullSummary
from tabtool.services import DataService


@pytest.fixture
def empty_df():
    return pd.DataFrame({"id": [], "datetime": [], "description": []})

@pytest.fixture
def small_df():
    return pd.DataFrame({
        "id": [1,2,3,4,5,6,7], 
    "datetime": [datetime.datetime(1997, 12, 3), 
                datetime.datetime(1994, 6, 3), 
                datetime.datetime(1980, 10, 30), 
                datetime.datetime(2004, 1, 3), 
                datetime.datetime(2021, 11, 13), 
                datetime.datetime(2016, 4, 1), 
                datetime.datetime(2020, 2, 20),],
    "description": ["a", "b", "c", "d", "e", "f", "g"]})

def test_get_brief_info_empty_frame(empty_df):
    expected_info = BriefSummary(empty_df.describe(include="all"), empty_df, empty_df, 0)
    
    actual_info = DataService.get_brief_info(empty_df)

    print(actual_info.description)
    pdt.assert_frame_equal(actual_info.description, expected_info.description)
    pdt.assert_frame_equal(actual_info.head, expected_info.head)
    pdt.assert_frame_equal(actual_info.tail, expected_info.tail)
    assert actual_info.number_of_records == expected_info.number_of_records

def test_get_brief_info_small_df(small_df):
    
    small_df_summary = small_df.describe(include="all")
    expected_info = BriefSummary(small_df_summary, small_df.head(), small_df.tail(), 7)
    
    actual_info = DataService.get_brief_info(small_df)

    pdt.assert_frame_equal(actual_info.description, expected_info.description)
    pdt.assert_frame_equal(actual_info.head, expected_info.head)
    pdt.assert_frame_equal(actual_info.tail, expected_info.tail)
    assert actual_info.number_of_records == expected_info.number_of_records

def test_get_brief_info_large_df(): #todo: this should be streamed
    pass

def test_get_full_info_small_df(small_df):
    column_descriptions = {col : small_df[col].describe() for col in small_df.columns}
    small_df_summary = small_df.describe(include="all")
    brief_summary = BriefSummary(small_df_summary, small_df.head(), small_df.tail(), 7)
    
    expected_info = FullSummary(brief_summary, column_descriptions)
    expected_column_dfs = expected_info.column_info.values()    

    actual_info = DataService.get_all_info(small_df)
    actual_column_dfs = actual_info.column_info.values()

    pdt.assert_frame_equal(actual_info.brief.description, expected_info.brief.description)
    assert expected_info.column_info.keys() == actual_info.column_info.keys()
    for (expected_df, actual_df) in zip(expected_column_dfs, actual_column_dfs, strict=True):
        pdt.assert_series_equal(actual_df, expected_df)
    