from functools import cache


# def giai_thua(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n * giai_thua(n - 1)


# def chinh_hop(n: int, k: int) -> int:
#     return giai_thua(n)/(giai_thua(k)*giai_thua(n-k))


@cache
def chinh_hop(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    else:
        return chinh_hop(n-1, k) + chinh_hop(n-1, k-1)


if __name__ == "__main__":
    n = int(input("nhap so chinh hop di ban: "))
    k = int(input("nhap so chap di ban: "))
    print(int(chinh_hop(n, k)))
