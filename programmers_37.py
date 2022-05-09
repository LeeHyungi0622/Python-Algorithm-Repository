def solution(s):
    return int(s)


s = "-1234"
print(solution(s))
print(type(solution(s)))


# ===== 다른사람 풀이법

s = "-1234"


def solutions(s):
    result = 0

    # 인자로 받은 문자열을 거꾸로 뒤집어서 순회한다.
    for idx, number in enumerate(s[::-1]):
        if number == '-':
            result *= -1
        else:
            # 이 부분이 핵심인데, 뒤집어서 배열을 순회한 이유가 여기에 있다.
            # index가 0부터 순회를 시작하는데,
            # 10^0 ~ 10^len(s)까지 순회를 하면서 각 자리수를 곱해서 더해야되기 때문이다.
            # 그래서 자리수를 뒤집어서 끝자리부터 계산하도록 만들었다.
            result += int(number) * (10 ** idx)
    return result


print(solutions(s))
print(type(solutions(s)))
