from .GameFileAssistant import GameFileAssistant
from .AppTUI import AppTUI
from .Game import Game
from .GameTUI import GameTUI


class GameApp:
    def __init__(self) -> None:
        self.file_assistant = GameFileAssistant()
        self.app_tui = AppTUI()

        self.game = Game()
        self.game_tui = GameTUI()

    def start(self) -> None:
        self.main_cycle()

    def main_cycle(self) -> None:
        pass
