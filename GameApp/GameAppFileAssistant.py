import os
from typing import List, Callable, Iterable
from random import sample, choice

from .SubsidiaryFiles.Field import Field
from .SubsidiaryFiles.Cell import Cell, CellContent

FIELDS_DIR = "./Fields/"


class GameAppFileAssistant:
    def __init__(self) -> None:
        pass

    def get_fields_names(self) -> List[str]:
        if not os.access(path=FIELDS_DIR, mode=os.F_OK):
            os.mkdir(path=FIELDS_DIR)

        return sorted(os.listdir(path=FIELDS_DIR))

    def decode(self, field_file_name: str) -> Field:
        field_file_name = self.normalize(field_file_name)

        with open(field_file_name, mode="r") as field_file:
            lines: List[str] = list(map(str.strip, field_file.readlines()))
            line: str = lines[0]

            type_string: str = line[:10]
            opened_string: str = line[10:20]
            flagged_string: str = line[20:]

            func: Callable[[str], Iterable[int]] = lambda x: map(int, list(x))  # short func for "123"->[1, 2, 3]

            type_dict = dict()

            for x in func(type_string[:5]):
                type_dict[x] = CellContent.EMPTY
            for x in func(type_string[5:]):
                type_dict[x] = CellContent.MINE

            opened_dict = dict()

            for x in func(opened_string[:5]):
                opened_dict[x] = True
            for x in func(opened_string[5:10]):
                opened_dict[x] = False

            flagged_dict = dict()

            for x in func(flagged_string[:5]):
                flagged_dict[x] = True
            for x in func(flagged_string[5:10]):
                flagged_dict[x] = False

            matrix: List[List[Cell]] = list()
            for line in lines[1:]:
                line = line.strip()

                matrix.append(list())
                for i in range(0, len(line), 3):
                    type = int(line[i])
                    opened = int(line[i + 1])
                    flagged = int(line[i + 2])

                    matrix[len(matrix) - 1].append(Cell(type_dict[type], opened_dict[opened], flagged_dict[flagged]))

            return Field(matrix, self.normalize(field_file_name))

    def save_field(self, matrix: List[List[Cell]], field_file_name: str = "") -> None:
        if not field_file_name:
            last_index: int = 0
            for field_file_name in os.listdir(path=FIELDS_DIR):
                last_index = max(last_index, int(field_file_name.lstrip("Field").rstrip(".txt")))

            field_file_name = FIELDS_DIR + f"Field{last_index + 1}" + ".txt"
        else:
            field_file_name = self.normalize(field_file_name)
        # My strange algorithm to hide field content.
        # I select 5 different numbers for each type, state opened/closed, state flagged/not flagged,
        # write this numbers in the start of the file and then for each cell I select random number from selected
        # for 3 cell parameters

        # It is not the best way, but I just wrote what first came to mind
        # (I think, it is OK encrypting for this task)
        type_key_string: List[int] = sample([i for i in range(10)], k=10)
        opened_key_string: List[int] = sample([i for i in range(10)], k=10)
        flagged_key_string: List[int] = sample([i for i in range(10)], k=10)

        type_dict = dict()
        type_dict[CellContent.EMPTY] = type_key_string[:5]
        type_dict[CellContent.MINE] = type_key_string[5:]

        opened_dict = dict()
        opened_dict[True] = opened_key_string[:5]
        opened_dict[False] = opened_key_string[5:]

        flagged_dict = dict()
        flagged_dict[True] = flagged_key_string[:5]
        flagged_dict[False] = flagged_key_string[5:]

        with open(field_file_name, mode="w") as field_file:
            func = lambda x: "".join(map(str, x))
            field_file.write(func(type_key_string) + func(opened_key_string) + func(flagged_key_string) + "\n")

            field_file.write("\n".join(map(lambda row: "".join(
                map(lambda cell: str(choice(type_dict[cell.content])) + str(choice(opened_dict[cell.opened])) + str(
                    choice(flagged_dict[cell.flagged])), row)),
                                           matrix)))

    def delete(self, field_file_name: str) -> None:
        field_file_name = self.normalize(field_file_name)

        os.remove(field_file_name)

    @staticmethod
    def normalize(field_file_name: str) -> str:
        field_file_name: str = FIELDS_DIR + field_file_name if not field_file_name.startswith(
            FIELDS_DIR) else field_file_name
        field_file_name: str = field_file_name + ".txt" if not field_file_name.endswith(".txt") else field_file_name
        return field_file_name
