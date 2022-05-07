strings = ["abce", "abcd", "cdx"]


def solution(strings, n):
    sorted_lst = sorted([i[n]+i for i in strings])
    answer = [i[1:] for i in sorted_lst]
    return answer


print(solution(strings, 2))


# ------------모범답안 sorted with key=lambda 사용

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(strings, 2))


# -----------새롭게 쓰는 방법

def solutions(strings, n):
    def sortkey(x):
        return (x[n], x)
    strings.sort(key=sortkey)
    return strings


print(solutions(strings, 2))
