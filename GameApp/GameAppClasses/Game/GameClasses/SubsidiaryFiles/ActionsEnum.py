from enum import Enum


class Action(Enum):
    FLAG = "Put/remove flag"
    OPEN = "Open cell"
    AI_MOVE = "See AI move"
    FINISH = "Finish game (check all mines are flagged)"
    SAVE = "Save field"
    DELETE = "Delete this field"
