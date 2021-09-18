from typing import List
from .Cell import Cell


class Field:
    NEW = "0"

    def __init__(self, matrix: List[List[Cell]] = None, filename: str = NEW) -> None:
        self.matrix = matrix
        self.filename: str = filename

