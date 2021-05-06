from typing import List


def selection_sort(mang: List[int]):
    phan_tu = len(mang)
    for i in range(phan_tu):
        min = i
        for j in range(i+1, phan_tu):
            if mang[j] < mang[min]:
                min = j
        mang[i], mang[min] = mang[min], mang[i]

if __name__ == "__main__":
    mang = [3, 5, 6, 1, -10, -11, 8, 9, 4, 7]
    selection_sort(mang)
    print(mang)
