def is_leap_year():
    y = int(input("연도를 입력하세요: "))
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False
    print(f"{y}년은 윤년입니다." if result else f"{y}년은 윤년이 아닙니다.")
    return result

is_leap_year()