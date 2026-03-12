from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class FileFormat(str, Enum):
    csv = "csv"
    json = "json"
    parquet = "parquet"
    orc = "orc"
    avro = "avro" # TODO: read first
    unsupported = ""

class FileCompression(str, Enum):
    gz = "gz"
    tar = "tar"
    zip = "zip"
    zstd = "zstd"
    bz2 = "bz2"
    xz = "xz"
    none = ""

@dataclass(frozen=True, slots=True)
class Filename:
    path : str
    base_name : str
    extension : FileFormat
    compression : FileCompression

    def get_file_path(self):
        compression_postfix = "" if self.compression == "" else "." + self.compression
        suffix = "." + self.extension + compression_postfix
        return Path(self.path, self.base_name).with_suffix(suffix)
