def sum_n():
    n = int(input("정수 n을 입력하세요: "))
    s = 0
    for i in range(1, n + 1):
        s += i
    print(f"1부터 {n}까지의 합은 {s}입니다.")