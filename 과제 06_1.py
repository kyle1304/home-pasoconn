def average():
    nums = input("숫자들을 입력하세요 (숫자와 숫자 사이에는 공백을 두세요): ").split()
    nums = [int(num) for num in nums]
    if not nums:
        return 0
    result = sum(nums) / len(nums)
    print(f"평균: {result}")
    return result

average()