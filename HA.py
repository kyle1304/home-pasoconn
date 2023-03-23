def gugudan():
    dan = int(input("출력할 구구단을 입력하세요: "))
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


def c2f():
    t_c = float(input("섭씨 온도를 입력하세요: "))
    t_f = (9 / 5) * t_c + 32
    print(f"섭씨 {t_c}도는 화씨 {t_f}도입니다.")


def sum_n():
    n = int(input("정수 n을 입력하세요: "))
    s = 0
    for i in range(1, n + 1):
        s += i
    print(f"1부터 {n}까지의 합은 {s}입니다.")
