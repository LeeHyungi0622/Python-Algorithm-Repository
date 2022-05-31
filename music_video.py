# 곡 수 : N, DVD 갯 수 : M
# N, M = map(int, input().split(' '))
# num_lst = list(map(int, input().split()))

def Count(capacity):
    cnt = 1
    sum = 0
    for x in num_lst:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


N = 9
M = 3

num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lt = 1
rt = sum(num_lst)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if Count(mid) <= M:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
