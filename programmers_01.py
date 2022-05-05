lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]


def solution(lottos, win_nums):
    answer = [6, 6, 5, 4, 3, 2, 1]

    lottos_set = set(lottos)
    win_nums_set = set(win_nums)

    lcnt = len(lottos_set.intersection(win_nums_set))
    hcnt = lcnt + lottos.count(0)

    return answer[hcnt], answer[lcnt]


print(solution(lottos, win_nums))


# 모범답안

def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


print(solution(lottos, win_nums))
