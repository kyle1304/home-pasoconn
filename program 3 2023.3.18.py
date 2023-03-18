food_calorie = {
    "사과": 52,
    "바나나": 89,
    "치즈": 402,
    "햄버거": 295,
    "감자튀김": 312
}

food = input("음식 이름을 입력하세요: ")

if food in food_calorie:
    calorie = food_calorie[food]
    print(f"{food}의 칼로리는 {calorie}kcal입니다.")
else:
    print("해당 음식의 칼로리 정보를 찾을 수 없습니다.")