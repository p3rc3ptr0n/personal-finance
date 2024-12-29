from glob import glob
from typing import List
from numbers_parser import Document
import pandas


def read_numbers_file(file_path: str) -> pandas.DataFrame:
    doc = Document(file_path)
    sheets = doc.sheets
    tables = sheets[1].tables
    data = tables[0].rows(values_only=True)
    return pandas.DataFrame(data[1:], columns=data[0])


def read_directory(dir_path: str, file_type: str = "numbers") -> List[pandas.DataFrame]:
    file_list = glob(f"{dir_path}/*.{file_type}")
    if file_list:
        return [read_numbers_file(fn) for fn in file_list]
    else:
        Warning(f"No files found in [{dir_path}] for type [{file_type}].")


def read_directory_and_concatenate_tables(dir_path: str) -> pandas.DataFrame:
    tables = read_directory(dir_path)
    return pandas.concat(tables, axis=0)
