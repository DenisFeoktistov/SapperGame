from enum import IntEnum


class CellContent(IntEnum):
    EMPTY = 0
    FLAG = 1
    MINE = 2


class Cell:
    def __init__(self, content: CellContent = CellContent.EMPTY, opened: bool = False) -> None:
        self.content: CellContent = content
        self.opened = opened
