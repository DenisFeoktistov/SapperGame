from .SubsidiaryFiles.input_output_functions.colorized import colorized, Colors
from GameApp.GameAppClasses.GameAppFileAssistant import GameAppFileAssistant
from GameApp.GameAppClasses.AppTUI import AppTUI, CREATE_NEW_FIELD
from GameApp.SubsidiaryFiles.generate_field import generate_field
from GameApp.GameAppClasses.Game.Game import Game
from GameApp.SubsidiaryFiles.Field import Field


class GameApp:
    def __init__(self) -> None:
        self.file_assistant = GameAppFileAssistant()
        self.app_tui = AppTUI(self.file_assistant)

        self.game = Game()

    def start(self) -> None:
        self.show_rules()
        self.main_cycle()

    def main_cycle(self) -> None:
        while True:
            field_file_name: str = self.app_tui.select_field_file()
            if field_file_name == CREATE_NEW_FIELD:
                self.file_assistant.save_field(
                    generate_field(*self.app_tui.select_field_settings()))

                field_file_name: str = self.file_assistant.get_fields_names()[-1]

            field: Field = self.file_assistant.decode(field_file_name)
            field, finished = self.game.game_cycle(field)

            if finished:
                self.file_assistant.delete(field.filename)
            else:
                self.file_assistant.save_field(field.matrix, field.filename)

    @staticmethod
    def show_rules() -> None:
        print(f"""{colorized("Sapper Game", Colors.GREEN)}

{colorized("Something you should know:", Colors.GREEN)} 
○ - closed cell.
{colorized("⚐", Colors.YELLOW)} - flag. You can put it on some position and put away (just put it twice on some cell).
{colorized("◉", Colors.RED)} - mine. You are going to see in case of mistake :).
0, 1, 2, 3... - number on cell will show how many mines around.

You are going to win if only you open all cells excepted mines. You can save your field at any moment and continue play later.

{colorized("Good luck!", Colors.GREEN)}""")
