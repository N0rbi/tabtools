from typing import Dict

from pandas import Series


class ColumnView:

    def __init__(self, column_name : str, column_info : Series):
        self._column_name = column_name
        self._column_info = column_info

    def show(self):
        print("Detailed description of " + self._column_name)
        print()
        print(self._column_info)
        print()
        print()

class ColumnListView:

    def __init__(self, columns : Dict[str, Series]):
        self._columns_views = [ColumnView(name, info) for name, info in columns.items()]

    def show(self):
        print()
        for column_view in self._columns_views:
            column_view.show()
        print()