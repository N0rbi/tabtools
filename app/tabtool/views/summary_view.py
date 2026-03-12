from ..models import BriefSummary, FullSummary
from . import ColumnListView


class BriefSummaryView:

    def __init__(self, summary: BriefSummary):
        self._summary = summary

    def show(self):
        print(self._summary.description)
        print(self._summary.head)
        remaining_records = self._summary.get_remaining_records()
        if (remaining_records != -1):
            print()
            print("... " + str(remaining_records) + " more records ...")
            print()

        print(self._summary.tail)

class FullSummaryView:

    def __init__(self, summary: FullSummary):
        self._summary = summary
        self._brief_summary_view = BriefSummaryView(self._summary.brief)
        self._column_list_view = ColumnListView(self._summary.column_info)

    def show(self):
        self._brief_summary_view.show()
        self._column_list_view.show()
