
# 재귀함수로 풀이 (top-down - memoization)

cache = [-1] * 91 # -1이면 구한적이 없는 문
cache[0] = 0
cache[1] = 1

def f(n):
    if cache[n] < 0:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]

print(f(int(input())))

# 반복문으로 피보나치 수열 문제풀이(1)

cache = [0, 1]

for i in range(2, int(input())+1):
    cache.append(cache[i-1] + cache[i-2])

print(cache[-1])

# 반복문으로 피보나치 수열 문제풀이(2)

N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N])


# cache = [-1] * 91 # -1이면 구한적이 없는 문
# cache[0] = 0
# cache[1] = 1

# cnt = 0

# def f(n):
#     global cnt

#     cnt += 1
#     if cache[n] < 0:
#         cache[n] = f(n-1) + f(n-2)
#     return cache[n]

# print(f(int(input())))
# print(cache)
# print(f'cnt: {cnt}')



