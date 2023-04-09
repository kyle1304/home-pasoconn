def read_file(filename):
    rainfalls = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            line_num += 1
            if line_num == 1:
                continue
            # 방법 1
            # token = line.split(",")
            # print(tokens)

            #방법 2
            tokens = line.split(",")
            rainfall = float(tokens[9])
            rainfalls.append(rainfall)
            #print(rainfall)

    return rainfalls

def count_rain_days(rainfalls):
    count = 0
    for num in rainfalls:
        if num >= 0.1:
            count += 1

    return count

def longest_rain_days(rainfalls):
    rain_event_days = []
    rainday_count = 0
    for rainfall in rainfalls:
        if rainfall > 0:
            rainday_count += 1
        if rainfall == 0 and rainday_count > 0:
            rain_event_days.append(rainday_count)
            rainday_count = 0
    if rainday_count > 0:
        rain_event_days.append(rainday_count)

    return max(rain_event_days)


def max_rainfall_event(rainfalls):
    max_rainfall = 0
    current_rainfall = 0
    for rainfall in rainfalls:
        if rainfall > 0:
            current_rainfall += rainfall
            if current_rainfall > max_rainfall:
                max_rainfall = current_rainfall
        else:
            current_rainfall = 0
    return max_rainfall



def avg_temp(filename):
    total_temp = 0
    count = 0
    with open(filename) as f:
        line_num = 0
        for line in f:
            if line_num == 0:
                line_num += 1
                continue
            tokens = line.split(",")
            tavg = float(tokens[6])
            total_temp += tavg
            count += 1
    return total_temp / count


def max_temp(filename) :
    with open(filename) as f:
        line_num = 0
        max_temp_list = []
        for line in f:
            if line_num == 0:
                line_num += 1
                continue
            tokens = line.split(",")
            max_t = float(tokens[5])
            max_temp_list.append(max_t)
        max_temp_list = sorted(max_temp_list, reverse=True)
    return max_temp_list

def main():
    filename = "weather(146)_2022-2022.csv"
    rainfall = read_file(filename)

    #1)총 강수량은?
    print(f"총 강수량은 {sum(rainfall):.1f}mm입니다")
    #2) 강우 일수는?(1mm이상 온 날 수)
    print(f"총 강우 일수는 {count_rain_days(rainfall)}일입니다")


    #4) 최장 강우 일수는?
    print(f"최장 연속 강우 일수는 {longest_rain_days(rainfall)}일입니다")
    #5) 강우 이벤트 중 최대 강수량은?
    print(f"강우이벤트 중 최대  강수량은{max_rainfall_event(rainfall):.1f}mm입니다")

    # 과제09-1) 연평균기온(tavg의 평균)을 구하시오.
    print(f"연평균기온(tavg의 평균) 은 {avg_temp(filename):.1f}입니다")
    # 과제09-2) 가장 더운날 top3(max의 최댓값 3개)
    print(f"가장 더운날 top3(max의 최댓값 3개): {max_temp(filename) [:3]}")

if __name__ == "__main__":
    main()