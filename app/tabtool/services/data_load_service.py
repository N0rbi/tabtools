import pandas as pd

from ..models import FileFormat, Filename

PARSERS = {}

def register_parser(file_type):
    def decorator(fn):
        PARSERS[file_type] = fn
        return fn
    return decorator

@register_parser(FileFormat.csv)
def load_csv(filename : str):
    return pd.read_csv(filename)

@register_parser(FileFormat.json)
def load_json(filename : str):
    return pd.read_json(filename)

@register_parser(FileFormat.parquet)
def load_parquet(filename : str):
    return pd.read_parquet(filename) 

@register_parser(FileFormat.orc)
def load_orc(filename : str):
    return pd.read_orc(filename)

class DataLoadService:

    @staticmethod
    def load_file(filename: Filename) -> pd.DataFrame:
        return PARSERS[filename.extension](filename.get_file_path())