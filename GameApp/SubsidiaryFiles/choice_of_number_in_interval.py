EMPTY_INTERVAL = -(10 ** 9 + 7)


def choice_of_number_in_interval(interval_min: int, interval_max: int, text: str = "Choose number in interval",
                                 error_message="Incorrect input! Try again") -> int:
    if interval_min > interval_max:
        print("No possible options...")
        return EMPTY_INTERVAL

    while True:
        try:
            print(text, f"({interval_min} <= number <= {interval_max}): ", end="")
            number: int = int(input())
            if number < interval_min or interval_max < number:
                raise Exception("Value not in interval")
            return number
        except Exception:
            print(error_message)
