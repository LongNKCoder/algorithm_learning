from typing import List


def interchange_sort(mang: List[int]) -> None:
    phan_tu = len(mang)
    for i in range(phan_tu):
        print(mang)
        for j in range(i+1, phan_tu):
            if mang[i] > mang[j]:
                mang[i], mang[j] = mang[j], mang[i]
    return None


if __name__ == "__main__":
    mang = [3, 5, 6, 1, 2, 0, 8, 9, 4, 7]
    interchange_sort(mang)
    print(mang)
