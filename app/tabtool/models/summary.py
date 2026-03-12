from dataclasses import dataclass
from typing import Dict

from pandas import DataFrame, Series


@dataclass(frozen=True, slots=True)
class BriefSummary:
    description : DataFrame
    head : DataFrame
    tail : DataFrame
    number_of_records : int

    def get_remaining_records(self):
        values_shown = len(self.head) + len(self.tail)
        if values_shown > self.number_of_records:
            return -1
        else:
            return self.number_of_records - values_shown

@dataclass(frozen=True, slots=True)
class FullSummary:
    brief : BriefSummary
    column_info : Dict[str, Series]

    