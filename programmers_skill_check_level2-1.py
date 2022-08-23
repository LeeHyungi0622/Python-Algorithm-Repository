from itertools import permutations


def is_prime_number(x):
    if x == 0 or x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    n = len(numbers)
    combination_idx = []
    for i in range(1, n + 1):
        combination_idx += permutations(range(n), i)

    result = []
    for idx in combination_idx:
        v = []
        for i in idx:
            v.append(numbers[i])
        result.append(int("".join(v)))

    result = set(result)

    for r in result:
        if is_prime_number(int(r)):
            print(r)
            answer += 1

    return answer


numbers = "011"

print(solution(numbers))
