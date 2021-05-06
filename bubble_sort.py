from typing import List


def bubble_sort(mang: List[int]) -> None:
    phan_tu = len(mang)
    for i in range(phan_tu):
        for j in range(phan_tu - 1, i, -1):
            if mang[j] < mang[j-1]:
                mang[j], mang[j-1] = mang[j-1], mang[j]

if __name__ == "__main__":
    mang = [3, 5, 6, 1, 2, 0, 8, 9, 4, 7]
    bubble_sort(mang)
    print(mang)
