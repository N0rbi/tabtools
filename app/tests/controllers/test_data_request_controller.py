from unittest.mock import MagicMock, patch

import pytest

from tabtool.controllers import DataRequestController
from tabtool.models import FileCompression, FileFormat, Filename, Options

import tabtool


@pytest.fixture
def request_controller_mocks():
    fake_df = MagicMock()

    controller_path = "tabtool.controllers.data_request_controller."
    data_service = controller_path + "DataService."

    load_file_patch = patch(controller_path + "DataLoadService.load_file", return_value=fake_df)
    
    brief_patch = patch(data_service + "get_brief_info", return_value="summary")
    columns_patch = patch(data_service + "get_info_for_columns", return_value="summary_col")
    all_info_patch = patch(data_service + "get_all_info", return_value="summary_all")
    
    col_list_view_patch = patch(controller_path + "ColumnListView")
    full_view_patch = patch(controller_path + "FullSummaryView")
    brief_view_patch = patch(controller_path + "BriefSummaryView")

    with load_file_patch as load_mock, \
         brief_patch as brief_mock, \
         columns_patch as column_service_mock, \
         all_info_patch as all_service_mock, \
         col_list_view_patch as column_view_mock, \
         full_view_patch as full_view_mock, \
         brief_view_patch as brief_view_mock:

        yield {
            "fake_df": fake_df,
            "load": load_mock,
            "brief_service": brief_mock,
            "get_info_for_columns": column_service_mock,
            "get_all_info": all_service_mock,
            "brief_view": brief_view_mock,
            "column_view": column_view_mock,
            "full_view": full_view_mock,
        }

def test_brief_info_request(request_controller_mocks):
    print(tabtool.__file__)
    sample_filename = Filename("path/to/file", "file", FileFormat.csv, FileCompression.gz) 
    sample_option = Options("path/to/file/file.csv.gz", False, [], False)

    DataRequestController.handle_request(sample_filename, sample_option)

    request_controller_mocks["load"].assert_called_once_with(sample_filename)
    request_controller_mocks["brief_service"].assert_called_once_with(request_controller_mocks["fake_df"])
    request_controller_mocks["brief_view"].assert_called_once_with("summary")


def test_column_info_request(request_controller_mocks):
    sample_filename = Filename("path/to/file", "file", FileFormat.csv, FileCompression.gz) 
    sample_option = Options("path/to/file/file.csv.gz", False, ["col1", "col2"], False)

    DataRequestController.handle_request(sample_filename, sample_option)

    request_controller_mocks["load"].assert_called_once_with(sample_filename)
    request_controller_mocks["get_info_for_columns"] \
            .assert_called_once_with(request_controller_mocks["fake_df"], ["col1", "col2"])
    request_controller_mocks["column_view"].assert_called_once_with("summary_col")


def test_all_info_request(request_controller_mocks):
    sample_filename = Filename("path/to/file", "file", FileFormat.csv, FileCompression.gz) 
    sample_option = Options("path/to/file/file.csv.gz", True, [], False)

    DataRequestController.handle_request(sample_filename, sample_option)

    request_controller_mocks["load"].assert_called_once_with(sample_filename)
    request_controller_mocks["get_all_info"].assert_called_once_with(request_controller_mocks["fake_df"])
    request_controller_mocks["full_view"].assert_called_once_with("summary_all")