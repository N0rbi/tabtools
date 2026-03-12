from pathlib import Path

from ..models import FileCompression, FileFormat, Filename


class FileService:

    @staticmethod
    def parse_file(file_path : Path) -> Filename:
        if not FileService.exists(file_path):
            raise ValueError("File does not exist")

        path : str = str(file_path.parent)
        base_name : str = file_path.with_suffix("").stem

        num_suffixes : int = len(file_path.suffixes)

        extension : FileFormat = FileFormat.unsupported
        compression : FileCompression = FileCompression.none

        if num_suffixes == 2: 
            extension = FileFormat(file_path.suffixes[-2][1:])
            compression = FileCompression(file_path.suffixes[-1][1:])
        elif num_suffixes == 1:
            extension = FileFormat(file_path.suffixes[-1][1:])
            compression = FileCompression.none
        else:
            raise ValueError("Invalid file name")

        return Filename(path, base_name, extension, compression)

    @staticmethod
    def exists(file_path: Path) -> bool:
        return file_path.exists()