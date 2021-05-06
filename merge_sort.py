from typing import List


def merge(mang: List[int], left: int, mid: int, right: int) -> None:
    tmp = [x for x in range(right - left + 1)]
    pos = 0
    i = left
    j = mid + 1
    while not(i > mid and j > right):
        if (i <= left and j <= right and mang[i] < mang[j]) or j > right:
            tmp[pos] = mang[i]
            pos += 1
            i += 1
        else:
            tmp[pos] = mang[j]
            pos += 1
            j += 1
    for i in range(len(tmp)):
        mang[left + i] = tmp[i]


def merge_sort(mang: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    mid = int((left + right) / 2)
    merge_sort(mang, left, mid)
    merge_sort(mang, mid + 1, right)
    merge(mang, left, mid, right)


if __name__ == "__main__":
    mang = [9,6,7,0,8,5,6,4,3,2,1]
    merge_sort(mang, 0, len(mang) - 1)
    print(mang)
