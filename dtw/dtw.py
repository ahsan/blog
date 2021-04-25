from typing import List
import math


def distance(a: int, b: int) -> float:
    return math.sqrt((b**2)-(a**2))


def DTW(s: List[int], t: List[int]):
    num_rows, num_cols = len(s), len(t)

    _dtw = [[math.inf for _ in range(num_cols + 1)]
            for _ in range(num_rows + 1)]
    _dtw[0][0] = 0

    for i in range(num_rows):
        for j in range(num_cols):
            cost = distance(s[i], t[j])
            _dtw[i+1][j+1] = cost + min(_dtw[i][j+1], _dtw[i+1][j], _dtw[i][j])
    return _dtw[-1][-1]


if __name__ == "__main__":
    # s = [0, 1, 2, 3, 1]
    # t = [1, 2, 3, 1, 0]
    s = [1, 3, 4, 9, 8, 2, 1, 5, 7, 3]
    t = [1, 6, 2, 3, 0, 9, 4, 3, 6, 3]
    dtw = DTW(s, t)
    assert dtw == 15.0
    print(dtw)
