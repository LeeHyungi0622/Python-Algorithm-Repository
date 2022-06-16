import sys

MOD = 10007
#10의 7승으로 재귀 제한을 늘려준다.
sys.setrecursionlimit(10 ** 7)

cache = [[0] * 1001 for _ in range(1001)]

N, K = map(int, input().split())

def bino(n, k):
    if cache[n][k]:
        return cache[n][k]

    if k == 0 or k == n:
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n-1, k-1) + bino(n-1, k)

    return cache[n][k]

print(bino(N, K) % MOD)


# 반복문으로 풀이

MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]
N, K = map(int, input().split())

for i in range(1001):
    # 삼각수의 좌/우의 리스트 값을 1로 채워준다.
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD
for i in range(7):
    print(cache[i])
    
print()
print(cache[N][K])