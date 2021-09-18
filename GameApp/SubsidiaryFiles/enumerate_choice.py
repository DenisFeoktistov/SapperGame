from typing import List

EMPTY_OPTIONS_LIST = -1


def enumerate_choice(options: List[str] = None, text: str = "Select option:",
                     error_message="Incorrect input! Try again") -> int:
    if not options:
        print("No possible options...")
        return EMPTY_OPTIONS_LIST

    print(text)
    for i, option in enumerate(options):
        print(f"Option {i + 1}: {option}")

    while True:
        try:
            index: int = int(input())
            if index < 1 or index > len(options):
                raise Exception("Incorrect index")
            return int(input())
        except Exception:
            print(error_message)
