from typing import Tuple, List
from random import sample

from ....SubsidiaryFiles.get_table_neighbors import get_table_neighbors
from GameApp.SubsidiaryFiles.Cell import Cell, CellContent
from GameApp.SubsidiaryFiles.Field import Field
from .SubsidiaryFiles.ActionsEnum import Action


class AI:
    def __init__(self) -> None:
        self.field: Field = None

    def set_field(self, field: Field) -> None:
        self.field = field

    def get_move(self) -> Tuple[int, int]:
        p_matrix: List[List[float]] = [[-1] * self.field.get_size()[1] for _ in range(self.field.get_size()[0])]

        possible_mines_around: List[List[int]] = [[-1] * self.field.get_size()[1] for _ in
                                                  range(self.field.get_size()[0])]
        unopened_cells_around: List[List[int]] = [[-1] * self.field.get_size()[1] for _ in
                                                  range(self.field.get_size()[0])]

        for i, row in enumerate(self.field.matrix):
            for j, cell in enumerate(row):
                possible_mines_around[i][j] = cell.mines_around
                unopened_cells_around[i][j] = 0

                for ui, uj in get_table_neighbors(i, j, *self.field.get_size()):
                    u_cell = self.field.matrix[ui][uj]
                    if u_cell.opened:
                        if u_cell.content == CellContent.MINE:
                            possible_mines_around[i][j] -= 1
                    else:
                        if u_cell.flagged:
                            possible_mines_around[i][j] -= 1
                        unopened_cells_around[i][j] += 1

        for i, row in enumerate(self.field.matrix):
            for j, cell in enumerate(row):
                for ui, uj in get_table_neighbors(i, j, *self.field.get_size()):
                    p_matrix[ui][uj] = max(p_matrix[ui][uj],
                                           possible_mines_around[i][j] * 100 / unopened_cells_around[i][j])

        for i, row in enumerate(self.field.matrix):
            for j, cell in enumerate(row):
                if p_matrix[i][j] == -1:
                    p_matrix[i][j] = 101

        return sorted(sample(
            [(i, j, p_matrix[i][j]) for i in range(self.field.get_size()[1]) for j in range(self.field.get_size()[0])],
            k=self.field.get_size()[0] * self.field.get_size()[1]), key=lambda x: x[2])[0][0:2]
