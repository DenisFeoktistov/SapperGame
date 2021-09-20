import os
from typing import List
from random import sample, randint, choice

from .SubsidiaryFiles.Field import Field
from .SubsidiaryFiles.Cell import Cell, CellContent

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
        if not field_file_name.startswith(FIELDS_DIR):
            field_file_name = FIELDS_DIR + field_file_name

        with open(field_file_name, mode="r") as field_file:
            line = field_file.readline()

            key_string1 = line[0:9]
            key_string2 = line[9:19]
            line = line[19:]

            func = lambda x: map(int, list(x))  # short lambda for "123" -> [1, 2, 3]

            type_dict = dict()

            for x in func(key_string1[:3]):
                type_dict[x] = CellContent.EMPTY
            for x in func(key_string1[3:6]):
                type_dict[x] = CellContent.FLAG
            for x in func(key_string1[6:9]):
                type_dict[x] = CellContent.MINE

            opened_dict = dict()

            for x in func(key_string2[:5]):
                opened_dict[x] = True
            for x in func(key_string2[5:9]):
                opened_dict[x] = False

            matrix: List[List[Cell]] = list()
            for line in field_file.readlines():
                line = line.strip()
                matrix.append(list())
                for i in range(len(line), 2):
                    type = int(line[i])
                    opened = int(line[i + 1])
                    matrix[len(matrix) - 1].append(Cell(type_dict[type], opened_dict[opened]))

            f = Field(matrix, field_file_name)
            print(f)
            return Field(matrix, FIELDS_DIR + field_file_name)

    def save_field(self, matrix: List[List[Cell]]) -> None:
        last_index = 0
        for field_file_name in os.listdir(path=FIELDS_DIR):
            last_index = max(last_index, int(field_file_name.lstrip("Field").rstrip(".txt")))

        # My strange algorithm to hide field content.
        # I select 3 different numbers for each type, 5 different numbers for each state opened/closed,
        # write this numbers in the start of the file and then for each cell I select random number from selected
        # for two cell parameters

        # It is not the best way, but I just wrote what first came to mind
        # (I think, it is OK encrypting for this task, so...)
        key_string1 = sample([i for i in range(9)], k=9)
        key_string2 = sample([i for i in range(10)], k=10)

        type_dict = dict()
        type_dict[CellContent.EMPTY] = key_string1[:3]
        type_dict[CellContent.FLAG] = key_string1[3:6]
        type_dict[CellContent.MINE] = key_string1[6:]

        opened_dict = dict()
        opened_dict[True] = key_string2[:5]
        opened_dict[False] = key_string2[5:]

        with open(FIELDS_DIR + f"Field{last_index + 1}" + ".txt", mode="w") as field_file:
            field_file.write("".join(map(str, key_string1)) + "".join(map(str, key_string1)) + "\n")

            field_file.write("\n".join(map(lambda row: "".join(
                map(lambda cell: str(choice(type_dict[cell.content])) + str(choice(opened_dict[cell.opened])), row)),
                                         matrix)))
