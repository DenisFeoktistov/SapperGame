from .SubsidiaryFiles.Cell import Cell, CellContent
from typing import List
from random import sample


class FieldGenerator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_field(x: int, y: int, mines: int) -> List[List[Cell]]:
        mines_positions = sample([(i, j) for i in range(x) for j in range(y)], x * y)[:mines]

        return [[Cell(CellContent.MINE) if (i, j) in mines_positions else Cell(CellContent.EMPTY)
                 for i in range(x)]
                for j in range(y)]
