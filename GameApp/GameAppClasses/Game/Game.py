from __future__ import annotations
from typing import Tuple

from GameApp.GameAppClasses.Game.GameClasses.FieldInterface import FieldInterface, State
from GameApp.GameAppClasses.Game.GameClasses.GameTUI import GameTUI, Action
from GameApp.SubsidiaryFiles.input_output_functions.colorized import colorized, Colors
from .GameClasses.AI import AI
from GameApp.SubsidiaryFiles.Field import Field


class Game:
    def __init__(self) -> None:
        self.game_tui = GameTUI()
        self.field_interface = FieldInterface()
        self.AI = AI()

    def game_cycle(self, field: Field) -> Tuple[Field, bool]:
        state: State = self.field_interface.set_field(field)
        self.AI.set_field(field)

        last_action_AI: bool = False
        while True:
            if not last_action_AI:
                print(colorized("Actual field:", Colors.BLUE))
                print(field)

            last_action_AI = False

            action_tuple: Tuple[int, int, Action] = self.game_tui.get_action(*reversed(field.get_size()))
            x, y, action = action_tuple
            x -= 1
            y -= 1

            if action == Action.SAVE:
                return field, False

            if action == Action.DELETE:
                return field, True

            if action == Action.AI_MOVE:
                self.show_AI_move()
                last_action_AI = True
                continue

            if action == Action.FINISH:
                state = self.field_interface.finish_game()

            if action == Action.OPEN:
                state = self.field_interface.open(y, x)
            if action == Action.FLAG:
                state = self.field_interface.flag(y, x)

            # --------------------------------------------------------

            if state == State.WIN:
                print(colorized("Congrats! You win!", Colors.GREEN))
                return field, True
            if state == State.LOSE:
                print(colorized("Ooops! It was mistake!", Colors.RED))
                self.field_interface.open_field()
                print(colorized("Field arrangement:", Colors.BLUE))
                print(field)
                return field, True

            if state == State.MOVE_DONE:
                print(colorized(state.value, Colors.GREEN))
            elif state == State.INCORRECT_MOVE:
                print(colorized(state.value, Colors.RED))
            else:
                print(state.value)

    def show_AI_move(self):
        AI_move: Tuple[int, int, Action] = self.AI.get_move()
        if AI_move[2] == Action.OPEN:
            print(colorized(f"Open cell on position {(AI_move[0] + 1, AI_move[1] + 1)}", Colors.BLUE))
        elif AI_move[2] == Action.FLAG:
            print(colorized(f"Put flag on position {(AI_move[0] + 1, AI_move[1] + 1)}", Colors.BLUE))
