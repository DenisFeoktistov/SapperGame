from typing import List, Tuple


from input_output_functions.choice_of_number_in_interval import choice_of_number_in_interval
from GameApp.GameAppClasses.GameAppFileAssistant import GameAppFileAssistant
from input_output_functions.enumerate_choice import enumerate_choice
from input_output_functions.colorized import colorized, Colors

CREATE_NEW_FIELD = "Create new field"

DEFAULT_FIELD_DICT = dict()
DEFAULT_FIELD1 = "Field 5x5 size with 5 mines"
DEFAULT_FIELD_DICT[DEFAULT_FIELD1] = (5, 5, 5)
# it is possible to add some more default fields

CUSTOM = "Custom field"


class AppTUI:
    def __init__(self, file_assistant: GameAppFileAssistant) -> None:
        self.file_assistant = file_assistant

    def select_field_file(self) -> str:
        fields: List[str] = self.file_assistant.get_fields_names()

        chosen_field_index = enumerate_choice(
            list(map(lambda field: field, fields)) + [CREATE_NEW_FIELD], text=colorized("Select field:", Colors.BLUE))
        if chosen_field_index == len(fields):
            return CREATE_NEW_FIELD
        return fields[chosen_field_index]

    @staticmethod
    def select_field_settings() -> Tuple[int, int, int]:
        # Field info: (x-size, y-size, number of bombs)
        field_settings_options = [DEFAULT_FIELD1, CUSTOM]
        field_settings = field_settings_options[
            enumerate_choice(field_settings_options, text=colorized("Select field:", Colors.BLUE))]

        if field_settings == CUSTOM:
            x = choice_of_number_in_interval(5, 9, text=colorized("Select field x-size", Colors.BLUE))
            y = choice_of_number_in_interval(5, 9, text=colorized("Select field y-size", Colors.BLUE))
            mines = choice_of_number_in_interval(3, int(x * y * 0.3),
                                                 text=colorized("Select number of bombs", Colors.BLUE))

            return x, y, mines
        else:
            return DEFAULT_FIELD_DICT[field_settings]
