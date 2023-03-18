bmi = float(input("BMI를 입력하세요: "))

if bmi < 18.5:
    print("저체중입니다.")
elif bmi < 23:
    print("정상체중입니다.")
elif bmi < 25:
    print("비만 전단계입니다.")
elif bmi < 30:
    print("1단계 비만입니다.")
elif bmi < 35:
    print("2단계 비만입니다.")
else:
    print("3단계 비만입니다.")