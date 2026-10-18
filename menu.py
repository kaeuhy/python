def menu():
    print("1. 섭씨 온도 -> 화씨 온도")
    print("2. 화씨 온도 -> 섭씨 온도")
    print("3. 종료")
    return int(input("메뉴를 선택하세요: "))

def ctof(c):
    return c * 9.0 / 5.0 + 32

def ftoc(f):
    return (f - 32.0) * 5.0 / 9.0

def main():
    while True:
        index = menu()
        if index == 1:
            t = float(input("섭씨 온도를 입력하시오: "))
            print("화씨 온도 =", ctof(t), "\n")
        elif index == 2:
            c = float(input("화씨 온도를 입력하시오: "))
            print("섭씨 온도 = ", round(ftoc(c), 2), "\n")
        else:
            break

main()