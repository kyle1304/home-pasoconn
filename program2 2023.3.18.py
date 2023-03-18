x = float(input("x 좌표를 입력하세요: "))
y = float(input("y 좌표를 입력하세요: "))

if x > 0 and y > 0:
    print("입력한 좌표는 1사분면입니다.")
elif x < 0 and y > 0:
    print("입력한 좌표는 2사분면입니다.")
elif x < 0 and y < 0:
    print("입력한 좌표는 3사분면입니다.")
elif x > 0 and y < 0:
    print("입력한 좌표는 4사분면입니다.")
else:
    print("원점입니다.")