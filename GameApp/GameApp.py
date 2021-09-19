from .GameAppFileAssistant import GameAppFileAssistant
from .AppTUI import AppTUI, CREATE_NEW_FIELD
from GameApp.Game.Game import Game
from .FieldGenerator import FieldGenerator
from .SubsidiaryFiles.Field import Field


class GameApp:
    def __init__(self) -> None:
        self.file_assistant = GameAppFileAssistant()
        self.app_tui = AppTUI(self.file_assistant)
        self.field_generator = FieldGenerator()

        self.game = Game()

    def start(self) -> None:
        self.main_cycle()

    def main_cycle(self) -> None:
        while True:
            field_file_name: str = self.app_tui.select_field_file()
            while field_file_name == CREATE_NEW_FIELD:
                self.file_assistant.save_field(
                    self.field_generator.generate_field(*self.app_tui.select_field_settings()))

                field_file_name: str = self.app_tui.select_field_file()

            field: Field = self.file_assistant.decode(field_file_name)

            self.game.start(field)
