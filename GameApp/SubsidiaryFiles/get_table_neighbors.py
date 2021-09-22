from typing import List, Tuple


def get_table_neighbors(i: int, j: int, s1: int, s2: int) -> List[Tuple[int, int]]:
    return [(i1, j1) for i1 in range(max(0, i - 1), min(s1, i + 2)) for j1 in
            range(max(0, j - 1), min(s2, j + 2))]


# def get_table_neighbors1(i: int, j: int, s1: int, s2: int) -> List[Tuple[int, int]]:
#     res: List[Tuple[int, int]] = list()
#
#     if i > 0:
#         res.append((i - 1, j))
#     if i < s1 - 1:
#         res.append((i + 1, j))
#     if j > 0:
#         res.append((i, j - 1))
#     if j < s2 - 1:
#         res.append((i, j + 1))
#
#     return res
