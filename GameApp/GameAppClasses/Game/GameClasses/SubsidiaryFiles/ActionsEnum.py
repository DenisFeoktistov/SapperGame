from enum import Enum


class Action(Enum):
    FLAG = "Put flag"
    OPEN = "Open cell"
    SAVE = "Save field"
    AI_MOVE = "See AI move"
