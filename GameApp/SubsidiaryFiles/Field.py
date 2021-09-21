from typing import List, Tuple
from .Cell import Cell, CellContent
from .get_table_neighbors import get_table_neighbors2


class Field:
    NEW = "0"

    def __init__(self, matrix: List[List[Cell]] = None, filename: str = NEW) -> None:
        self.matrix = matrix
        self.filename: str = filename

        self.init_mines_around()

    def init_mines_around(self) -> None:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j].mines_around = 0

                for u in get_table_neighbors2(i, j, *self.get_size()):
                    self.matrix[i][j].mines_around += self.matrix[u[0]][u[1]].content == CellContent.MINE

    def __str__(self):
        res = str()
        res += "    " + " ".join(map(str, [i + 1 for i in range(len(self.matrix[0]))])) + "\n"
        res += "    " + "-" * (2 * len(self.matrix[0]) - 1) + "\n"
        for i, row in enumerate(self.matrix):
            res += f"{i + 1}"

            res += " | " + " ".join(map(str, row))
            if i != len(self.matrix) - 1:
                res += "\n"
        return res
        # return "\n".join(map(lambda row: "".join(map(str, row)), self.matrix))

    def get_size(self) -> Tuple[int, int]:
        return len(self.matrix), len(self.matrix[0])
