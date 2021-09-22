from enum import IntEnum


from GameApp.SubsidiaryFiles.input_output_functions.colorized import colorized, Colors


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

    def flag(self) -> None:
        self.flagged = not self.flagged

    def mark_as_flag(self) -> None:
        if not self.opened:
            self.flagged = True

    def __str__(self) -> str:
        if self.flagged and not self.opened:
            return colorized("⚐", Colors.YELLOW)
        if not self.opened:
            return "○"
        if self.content == CellContent.MINE:
            return colorized("◉", Colors.RED)
        if self.content == CellContent.EMPTY:
            if self.mines_around == -1:
                raise Exception("Init Cell with Field before calling __str__")
            return colorized(str(self.mines_around), Colors.GREEN)
