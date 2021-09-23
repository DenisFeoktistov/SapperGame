from typing import Tuple, List
from random import choice

from ....SubsidiaryFiles.get_table_neighbors import get_table_neighbors
from GameApp.SubsidiaryFiles.Cell import Cell, CellContent
from GameApp.SubsidiaryFiles.Field import Field
from .SubsidiaryFiles.ActionsEnum import Action


class AI:
    def __init__(self) -> None:
        self.field: Field = None

    def set_field(self, field: Field) -> None:
        self.field = field

    def get_move(self) -> Tuple[int, int, Action]:
        if self.all_closed():
            i, j = choice([(i, j) for i in range(self.field.get_size()[1]) for j in
                           range(self.field.get_size()[0])])

            return i, j, Action.OPEN

        p_matrix: List[List[int]] = [[-1] * self.field.get_size()[1] for _ in range(self.field.get_size()[0])]

        possible_mines_around: List[List[int]] = [[0] * self.field.get_size()[1] for _ in
                                                  range(self.field.get_size()[0])]
        unopened_cells_around: List[List[int]] = [[0] * self.field.get_size()[1] for _ in
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
                                           possible_mines_around[i][j] * 100 // unopened_cells_around[i][j])

        max_p: int = 0
        max_p_coords: Tuple[int, int] = (0, 0)
        for i, row in enumerate(self.field.matrix):
            for j, cell in enumerate(row):
                if p_matrix[i][j] > max_p and p_matrix[i][j] != -1:
                    max_p = p_matrix[i][j]
                    max_p_coords = i, j
        if max_p == 100:
            return max_p_coords[0], max_p_coords[1], Action.FLAG

        min_p: int = 0
        min_p_coords: Tuple[int, int] = (0, 0)
        for i, row in enumerate(self.field.matrix):
            for j, cell in enumerate(row):
                if p_matrix[i][j] < min_p and p_matrix[i][j] != -1:
                    min_p = p_matrix[i][j]
                    min_p_coords = i, j
        return min_p_coords[0], min_p_coords[1], Action.OPEN

    def all_closed(self) -> bool:
        return all(map(lambda row: all(map(lambda cell: not cell.opened, row)), self.field.matrix))
