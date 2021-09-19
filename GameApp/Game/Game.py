from GameApp.Game.GameTUI import GameTUI
from GameApp.Game.FieldInterface import FieldInterface


from ..SubsidiaryFiles.Field import Field


class Game:
    def __init__(self) -> None:
        self.game_tui = GameTUI()
        self.field_interface = FieldInterface()

    def start(self, field: Field) -> None:
        pass
