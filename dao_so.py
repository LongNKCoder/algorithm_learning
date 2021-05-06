def dao_so(chu_so: int):
    if chu_so/10 > 0:
        kq = int(chu_so % 10)
        print(kq, end="")
        dao_so(int(chu_so/10))


if __name__ == "__main__":
    number = int(input("nhap so tinh dao_so: "))
    dao_so(number)
