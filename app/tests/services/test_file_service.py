import pytest

from tabtool.models import FileCompression, FileFormat, Filename
from tabtool.services import FileService

from ..fake_classes import FakePath


def test_empty_path():
    test_path = FakePath("", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_file_not_exist():
    test_path = FakePath("path/to/file/non_existent.csv", False)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_invalid_file_extension_no_compression():
    test_path = FakePath("incorrect_extension.foo", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_invalid_file_extension_valid_compression():
    test_path = FakePath("incorrect_extension.foo.gz", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_missing_extension_with_compression():
    test_path = FakePath("incorrect_extension.gz", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)


def test_invalid_compression():
    test_path = FakePath("incorrect_compression.csv.bar", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_file_no_extension():
    test_path = FakePath("no_extension", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)

def test_file_too_many_extensions():
    test_path = FakePath("my_folder/too.many.extensions", True)

    with pytest.raises(ValueError):
        FileService.parse_file(test_path)


def test_valid_base_file():
    test_path = FakePath("path/to/file/correct_file_name.parquet", True)
    expected_fimename = Filename("path/to/file", "correct_file_name", 
            FileFormat.parquet, FileCompression.none)

    actual_filename = FileService.parse_file(test_path)

    assert actual_filename == expected_fimename


def test_vaild_compressed_file():
    test_path = FakePath("fullpath/to/file/correct_file_name_with_compression.json.zstd", True)
    expected_fimename = Filename("fullpath/to/file", "correct_file_name_with_compression", 
            FileFormat.json, FileCompression.zstd)

    actual_filename = FileService.parse_file(test_path)

    assert actual_filename == expected_fimename

