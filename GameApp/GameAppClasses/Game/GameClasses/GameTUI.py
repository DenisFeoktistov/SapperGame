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
        actions: List[Action] = [Action.OPEN, Action.FLAG, Action.SAVE, Action.AI_MOVE]
        action: Action = actions[
            enumerate_choice(list(map(lambda action: action.value, actions)), text=colorized("Make your move.", Colors.BLUE))]

        if action == Action.SAVE:
            return -1, -1, Action.SAVE

        if action == Action.AI_MOVE:
            return -1, -1, Action.AI_MOVE

        x: int = choice_of_number_in_interval(1, max_x, text=colorized("Select x", Colors.BLUE))
        y: int = choice_of_number_in_interval(1, may_y, text=colorized("Select y", Colors.BLUE))

        return x, y, action
