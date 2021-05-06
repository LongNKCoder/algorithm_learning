def print_arr(arr: list):
    for ele in arr:
        print(ele, end='\t')
    print()


def print_permutation(arr: list, i: int):
    print_arr(arr)
    j = i + 1
    for _ in range(j, len(arr)):
        if j > len(arr) - 1:
            return
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        print_permutation(arr, i + 1)
        j += 1

if __name__ == '__main__':
    arr = [10, 2, 5]
    print_permutation(arr, 0)
