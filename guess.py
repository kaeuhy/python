import random
random.seed(1)
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

score = 0
tries = 0
while answer != score:
    score = int(input("숫자를 입력하시오: "))
    tries += 1
    if answer > score:
        print("너무 낮음")
    elif answer < score:
        print("너무 높음")
print("축하합니다. 시도횟수 =", tries)