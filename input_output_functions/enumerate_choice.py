from typing import List

EMPTY_OPTIONS_LIST = -1


def enumerate_choice(options: List[str] = None, text: str = "Select option:",
                     error_message="Incorrect input! Try again") -> int:
    if not options:
        print("No possible options...")
        return EMPTY_OPTIONS_LIST

    while True:
        try:
            print(text)
            for i, option in enumerate(options):
                print(f"\tOption {i + 1}: {option}")
            index: int = int(input())
            if index < 1 or index > len(options):
                raise Exception("Incorrect index")
            return index - 1
        except Exception:
            print(error_message)
