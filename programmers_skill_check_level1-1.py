def solution(numbers):
    return sum(list(set([i for i in range(0, 10)]) - set(numbers)))


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
