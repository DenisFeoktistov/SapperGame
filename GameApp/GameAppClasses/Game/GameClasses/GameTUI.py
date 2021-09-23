from typing import Tuple, List

from GameApp.GameAppClasses.Game import Game
from GameApp.SubsidiaryFiles.input_output_functions.choice_of_number_in_interval import choice_of_number_in_interval
from GameApp.SubsidiaryFiles.input_output_functions.enumerate_choice import enumerate_choice
from GameApp.SubsidiaryFiles.input_output_functions.colorized import colorized, Colors
from GameApp.GameAppClasses.Game.GameClasses.SubsidiaryFiles.ActionsEnum import Action


class GameTUI:
    def __init__(self) -> None:
        pass

    def get_action(self, max_x, may_y) -> Tuple[int, int, Action]:
        actions: List[Action] = [Action.OPEN, Action.FLAG, Action.AI_MOVE, Action.FINISH, Action.SAVE, Action.DELETE]
        action: Action = actions[
            enumerate_choice(list(map(lambda action: action.value, actions)), text=colorized("Make your move.", Colors.BLUE))]

        if action == Action.SAVE or action == Action.DELETE or action == Action.AI_MOVE or action == Action.FINISH:
            return -1, -1, action

        x: int = choice_of_number_in_interval(1, max_x, text=colorized("Select x", Colors.BLUE))
        y: int = choice_of_number_in_interval(1, may_y, text=colorized("Select y", Colors.BLUE))

        return x, y, action
