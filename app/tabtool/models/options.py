from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, slots=True)
class Options:
    filename : str
    all_info : bool
    columns : List[str]
    performance_check : bool