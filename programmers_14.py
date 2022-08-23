def solution(nums):
    answer = 0
    variables = len(set(nums))
    num = len(nums) // 2

    if variables < num:
        answer = variables
    elif variables > num:
        answer = num
    else:
        answer = variables

    return answer


nums = [3, 1, 2, 3]

print(solution(nums))


def solution1(nums):
    return min(len(set(nums)), len(nums) / 2)


print(int(solution1(nums)))
