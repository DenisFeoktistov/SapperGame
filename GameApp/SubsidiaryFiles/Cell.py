from enum import IntEnum


class CellContent(IntEnum):
    EMPTY = 0
    MINE = 1


class Cell:
    def __init__(self, content: CellContent = CellContent.EMPTY, opened: bool = False, flagged: bool = False) -> None:
        self.content: CellContent = content
        self.opened: bool = opened
        self.flagged: bool = flagged

        self.mines_around: int = -1

    def open(self) -> None:
        self.opened = True
        self.flagged = False

    def mark_as_flag(self) -> None:
        if not self.opened:
            self.flagged = True

    def __str__(self) -> str:
        # if not self.opened:
        #     return "▆"
        if self.flagged:
            return "⚐"
        if self.content == CellContent.MINE:
            return "◉"
        if self.content == CellContent.EMPTY:
            return "▢"
