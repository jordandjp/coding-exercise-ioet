from os import PathLike
from typing import Union


def read_txt_employee_data(file: Union[str, bytes, PathLike]) -> list:
    """Read a .txt file into a list of raw strings representing timeslots entries"""
    with open(file, mode="rt", encoding="utf-8") as f:
        data = f.read().split("\n")
    return data
