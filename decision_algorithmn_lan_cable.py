K = [802, 743, 457, 539]
N = 11


def sol(mid):
    cnt = 0
    for i in K:
        cnt += (i // mid)
    return cnt


lt = 1
rt = max(K)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2

    if sol(mid) >= N:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)