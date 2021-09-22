from typing import List, Tuple
from random import sample


from GameApp.SubsidiaryFiles.Cell import Cell, CellContent


def generate_field(x: int, y: int, mines: int) -> List[List[Cell]]:
    mines_positions: List[Tuple[int, int]] = sample([(i, j) for i in range(x) for j in range(y)], x * y)[:mines]

    return [[Cell(CellContent.MINE) if (i, j) in mines_positions else Cell(CellContent.EMPTY)
             for i in range(x)]
            for j in range(y)]
