from math import gcd

# 최대공약수, 최소공배수 구하기
def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

print(solution(2, 5))
