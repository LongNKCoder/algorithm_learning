def sum(n: int):
    if n == 1:
        return n**2
    else:
        return n**2 + sum(n - 1)


if __name__ == "__main__":
    number = int(input("nhap so tinh tong: "))
    print(sum(number))
