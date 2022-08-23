from itertools import combinations


def solution(number):
    answer = 0

    combi_lst = list(combinations(number, 3))

    for c in combi_lst:
        if sum(c) == 0:
            answer += 1

    return answer


number = [-1, 1, -1, 1]

print(solution(number))
