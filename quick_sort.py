from typing import List


def quick_sort(mang: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    pivot = mang[int((left + right) / 2)]
    i = left; j= right
    while i <= j:
        while mang[i] < pivot: i += 1
        while mang[j] > pivot: j -= 1
        if i <= j:
            mang[i], mang[j] = mang[j], mang[i]
            i += 1
            j -= 1
    quick_sort(mang, left, j)
    quick_sort(mang, i, right)


if __name__ == "__main__":
    mang = [9,6,7,0,8,5,6,4,3,2,1]
    quick_sort(mang, 0, len(mang) - 1)
    print(mang)
