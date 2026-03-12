from ..models import Filename, Options
from ..services import DataLoadService, DataService
from ..views import BriefSummaryView, ColumnListView, FullSummaryView


class DataRequestController:

    @staticmethod
    def handle_request(filename : Filename, options : Options):
        data = DataLoadService.load_file(filename)
        is_brief_info_request = not options.columns and not options.all_info
        is_column_info_request = options.columns
        is_all_info_request = options.all_info

        if is_brief_info_request: 
            BriefSummaryView(DataService.get_brief_info(data)).show()
        elif is_column_info_request:
            ColumnListView(DataService.get_info_for_columns(data, options.columns)).show()
        elif is_all_info_request:
            FullSummaryView(DataService.get_all_info(data)).show()