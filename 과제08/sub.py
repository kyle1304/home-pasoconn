def read_numbers(filename):
    with open(filename, "r") as file:
        numbers = []
        for line in file:
            line = line.strip()
            if line:
                for num in line.split():
                    numbers.append(int(num))
        return numbers


def get_count(numbers):
    return len(numbers)


def get_mean(nums):
    if len(nums) == 0:
        return None
    total = sum(nums)
    count = len(nums)
    return total / count


def get_max_value(nums):
    if len(nums) == 0:
        return None
    return max(nums)


def get_min_value(nums):
    if len(nums) == 0:
        return None
    return min(nums)


def get_median_value(nums):
    sorted_nums = sorted(nums)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def main():
    filename = "numbers.txt"
    numbers = read_numbers(filename)
    print(f"총 숫자의 개수: {get_count(numbers)}")
    print(f"주어진 숫자의 평균: {get_mean(numbers):.1f}")
    print(f"주어진 숫자의 최댓값: {get_max_value(numbers)}")
    print(f"주어진 숫자의 최솟값: {get_min_value(numbers)}")
    print(f"중앙값: {get_median_value(numbers)}")


if __name__ == "__main__":
    main()