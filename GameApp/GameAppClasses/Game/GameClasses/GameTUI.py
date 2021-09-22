from typing import Tuple, List
from input_output_functions.enumerate_choice import enumerate_choice
from input_output_functions.choice_of_number_in_interval import choice_of_number_in_interval
from enum import Enum


class Action(Enum):
    FLAG = "Put flag"
    OPEN = "Open cell"
    SAVE = "Save field"


class GameTUI:
    def __init__(self) -> None:
        pass

    def get_action(self, max_x, may_y) -> Tuple[int, int, Action]:
        print("Make your move.")
        actions: List[Action] = [Action.OPEN, Action.FLAG, Action.SAVE]
        action: Action = actions[enumerate_choice(list(map(lambda action: action.value, actions)))]

        if action == Action.SAVE:
            return -1, -1, Action.SAVE

        x: int = choice_of_number_in_interval(1, max_x, text="Select x")
        y: int = choice_of_number_in_interval(1, may_y, text="Select y")

        return x, y, action
