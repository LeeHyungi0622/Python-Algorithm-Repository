def solution(brown, yellow):
    s = brown + yellow

    for a in range(s, 2, -1):
        if s % a == 0:
            b = s // a

            if (a - 2) * (b - 2) == yellow:
                return [a, b]


brown = 10
yellow = 2

print(solution(brown, yellow))
