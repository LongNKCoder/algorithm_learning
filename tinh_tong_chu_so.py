def sum(chu_so: int):
    kq = int(chu_so % 10)
    if int(chu_so/10) == 0:
        return kq
    return kq + sum(int(chu_so/10))


if __name__ == "__main__":
    number = int(input("nhap so tinh tong: "))
    print(sum(number))
