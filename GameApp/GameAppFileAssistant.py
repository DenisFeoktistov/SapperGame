import os
from typing import List


from .SubsidiaryFiles.Field import Field
from .SubsidiaryFiles.Cell import Cell


FIELDS_DIR = "./Fields/"


class GameAppFileAssistant:
    def __init__(self) -> None:
        pass

    def get_fields_names(self) -> List[str]:
        if not os.access(path=FIELDS_DIR, mode=os.F_OK):
            os.mkdir(path=FIELDS_DIR)

        return os.listdir(path=FIELDS_DIR)

    def get_fields(self) -> List[Field]:
        pass

    def decode(self, field_file_name: str) -> Field:
        pass

    def save_field(self, matrix: List[List[Cell]]) -> None:
        last_index = 0
        for field_file_name in os.listdir(path=FIELDS_DIR):
            last_index = max(last_index, int(field_file_name.lstrip("Field")))

        field = Field(matrix=matrix, filename=FIELDS_DIR + f"Field{last_index + 1}")
        with open(field.filename, mode="w") as field_file:
            field_file.write(str(field))
