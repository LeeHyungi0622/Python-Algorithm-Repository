from collections import defaultdict


def solution(topping):
    answer = 0
    yb = defaultdict(int)
    ob = defaultdict(bool)

    for t in topping:
        yb[t] = yb.get(t, 0) + 1

    for t in topping:
        yb[t] -= 1
        ob[t] = True

        if yb[t] == 0:
            del yb[t]

        if len(yb) == len(ob):
            answer += 1

    return answer


topping = [1, 2, 3, 1, 4]

print(solution(topping))
