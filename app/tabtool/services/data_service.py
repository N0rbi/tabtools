from typing import Dict, List

from pandas import DataFrame, Series

from ..models import BriefSummary, FullSummary


class DataService:

    @staticmethod
    def get_brief_info(data : DataFrame) -> BriefSummary:
        """
            Retuns: the description of the dataframe, the head, and the tail
        """

        summary = DataService._get_summary(data)
        head, tail = DataService._get_head(data), DataService._get_tail(data)
        lines = len(data)
        return BriefSummary(summary, head, tail, lines)
    
    @staticmethod
    def get_all_info(data : DataFrame) -> FullSummary:
        """
            Retuns: the description of the dataframe, 
            the head, and the tail, and the info for all columns
        """
        
        column_info = {name: DataService._get_column_info(data[name]) for name in data.columns}

        return FullSummary(DataService.get_brief_info(data), column_info)

    @staticmethod
    def get_info_for_columns(data : DataFrame, columns : List[str]) -> Dict[str, Series]:
        return {name: DataService._get_column_info(data[name]) \
                for name in data.columns if name in columns}
        
    @staticmethod
    def _get_head(df : DataFrame) -> DataFrame:
        return df.head()

    @staticmethod
    def _get_tail(df : DataFrame) -> DataFrame:
        return df.tail()

    @staticmethod
    def _get_summary(df : DataFrame) -> DataFrame:
        return df.describe(include="all")

    @staticmethod
    def _get_column_info(series : Series) -> Series:
        return series.describe()

    