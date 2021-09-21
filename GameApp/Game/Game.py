from GameApp.Game.GameTUI import GameTUI, Action
from GameApp.Game.FieldInterface import FieldInterface, State


from ..SubsidiaryFiles.Field import Field


from typing import Tuple, Type, Union


class Game:
    def __init__(self) -> None:
        self.game_tui = GameTUI()
        self.field_interface = FieldInterface()

    def game_cycle(self, field: Field) -> Tuple[Field, bool]:
        state: State = self.field_interface.set_field(field)

        while True:
            print("Actual field:")
            print(field)

            action_tuple: Tuple[int, int, Action] = self.game_tui.get_action(*reversed(field.get_size()))
            x, y, action = action_tuple
            x -= 1
            y -= 1
            if action == Action.SAVE:
                return field, False

            if action == Action.OPEN:
                state = self.field_interface.open(y, x)
            if action == Action.FLAG:
                state = self.field_interface.flag(y, x)

            if state == State.WIN:
                print("Congrats! You win!")
                print()
                return field, True
            if state == State.LOSE:
                print("Ooops! It was mistake!")
                self.field_interface.open_field()
                print("Field arrangement:")
                print(field)
                print()
                return field, True

            print(state.value)
