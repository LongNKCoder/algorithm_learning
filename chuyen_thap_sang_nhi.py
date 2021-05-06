

def chuyen_thap_nhi(number: int) -> int:
    if number > 0:
        sd = int(number % 2)
        number = int(number / 2)
        chuyen_thap_nhi(number)
        print(sd, end="")


if __name__ == "__main__":
    number = int(input("nhap so can doi: "))
    chuyen_thap_nhi(number)
