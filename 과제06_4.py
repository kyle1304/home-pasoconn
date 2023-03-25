def calculate_calories():
    fruits = {"딸기": 300, "한라봉": 150}
    total_calories = 0

    for i in range(2):
        fruit = input("과일 입력: ")
        weight = int(input("무게 입력(g): "))
        total_calories += fruits[fruit] * weight / 100

    print("총 칼로리: {:.2f} kcal".format(total_calories))

if __name__ == '__main__':
    calculate_calories()