from ..SubsidiaryFiles.Field import Field
from ..SubsidiaryFiles.Cell import Cell, CellContent
from enum import Enum
from typing import List, Tuple
from ..SubsidiaryFiles.get_table_neighbors import get_table_neighbors2


class State(Enum):
    FIELD_SET = ""
    MOVE_DONE = "Move done!"
    INCORRECT_MOVE = "Incorrect move!"
    WIN = "You won!"
    LOSE = "You lost"


class FieldInterface:
    def __init__(self) -> None:
        self.field: Field = None

    def set_field(self, field: Field) -> State:
        self.field = field

        return State.FIELD_SET

    def open_field(self) -> None:
        for row in self.field.matrix:
            for cell in row:
                cell.open()

    def open(self, i: int, j: int) -> State:
        cell: Cell = self.field.matrix[i][j]
        if cell.opened:
            return State.INCORRECT_MOVE
        else:
            if cell.content == CellContent.MINE:
                return State.LOSE
            else:
                if cell.mines_around == 0:
                    used = [[False] * len(self.field.matrix[0]) for _ in range(len(self.field.matrix))]
                    self.DFS_open(i, j, self.field, used)
                else:
                    cell.open()

            if self.check_win():
                return State.WIN
            else:
                return State.MOVE_DONE

    def DFS_open(self, i: int, j: int, field: Field, used: List[List[bool]]):
        field.matrix[i][j].open()
        used[i][j] = True

        neighbors: List[Tuple[int, int]] = get_table_neighbors2(i, j, *field.get_size())
        for ui, uj in neighbors:
            if used[ui][uj]:
                continue

            u_cell = field.matrix[ui][uj]

            if not u_cell.opened and u_cell.mines_around == 0:
                self.DFS_open(ui, uj, field, used)
            elif not u_cell.opened:
                u_cell.open()

    def flag(self, i: int, j: int) -> State:
        cell: Cell = self.field.matrix[i][j]
        cell.flag()
        return State.MOVE_DONE

    def check_win(self) -> bool:
        return all(map(lambda row: all(map(lambda cell: (cell.opened and cell.content == CellContent.EMPTY) or (
                not cell.opened and cell.content == CellContent.MINE), row)), self.field.matrix))
