from enum import IntEnum


class CellContent(IntEnum):
    EMPTY = 0
    FLAG = 1
    MINE = 2


class Cell:
    def __init__(self, content: CellContent = CellContent.EMPTY, opened: bool = False) -> None:
        self.content: CellContent = content
        self.opened = opened
        self.mines_around = -1

    def __str__(self) -> str:
        if self.content == CellContent.FLAG:
            return "⚐"
        if self.content == CellContent.MINE:
            return "💣"
        if self.content == CellContent.EMPTY:
            return "🗌"
