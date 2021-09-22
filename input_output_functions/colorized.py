from enum import Enum


class Colors(Enum):
    RESET = "\033[0;0m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"


def colorized(text: str, color: Colors) -> str:
    return color.value + text + Colors.RESET.value
