def gugudan():
    dan = int(input("출력할 구구단을 입력하세요: "))
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
