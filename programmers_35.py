def solution(n):
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    for i in range(2, n + 1):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    return len([i for i, v in enumerate(arr) if v == True])


print(solution(5))


# ==== 모범답안 더 간결하게 아리스토테네스의 체로 풀이하는 방법
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


print(solution(10))
