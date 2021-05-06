def move(n: int, thap_chinh: str, thap_trung_gian: str, thap_dich_den: str):  # muốn chuyển từ tháp chính sang tháp đích đến. Thì vòng đáy của tháp chính phải sang tháp đích
    if n == 1:
        print(f"{thap_chinh} ===> {thap_dich_den}: vong thu {n}")  # xác định vòng cuối của tháp chính
    else:
        move(n - 1, thap_chinh, thap_dich_den, thap_trung_gian)  # muốn đưa vòng cuối qua tháp đích thì phải đưa hết các vòng còn lại sang tháp trung gian
        print(f"{thap_chinh} ===> {thap_dich_den}: vong thu {n}")
        move(n - 1, thap_trung_gian, thap_chinh, thap_dich_den)  # chuyển những vòng còn lại từ tháp trung gian qua tháp đích


if __name__ == "__main__":
    number = int(input("nhap so vong: "))
    move(number, "A", "B", "C")
