from typing import Optional, Union
from inflection import camelize, underscore
import re


def split_name(value:Optional[str]):
    name_parts = re.split(r"\s+", (value or "").strip(), 1)
    if len(name_parts) == 2:
        return tuple(name_parts)
    return name_parts[0], ""

def strict_camelize(string:str, uppercase_first_letter=False):
    return camelize(underscore(string), uppercase_first_letter)