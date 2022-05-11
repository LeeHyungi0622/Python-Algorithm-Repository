import math


def lcm(a, b):
    return (a * b)//math.gcd(a, b)


def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(lcm(n, m))
    return answer


print(solution(2, 5))

# ==== 유클리드 호제법


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b)//gcd(a, b)


print(gcd(2, 5))
print(lcm(2, 5))


# ===== Euclidean algorithm을 활용한 또 다른 코드 작성

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))
