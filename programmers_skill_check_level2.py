from itertools import combinations


def solution(relation):
    # column의 수를 구해서 1부터 column의 수까지 i를 순회한다.
    # 후보키는 1개부터 전체 column의 수 만큼의 조합으로 구성될 수 있기 때문이다.
    n = len(relation[0])
    comb_idx = []
    for i in range(1, n + 1):
        comb_idx += list(combinations(range(n), i))

    check = []
    for idx in comb_idx:
        flag = False
        lst = []
        for person in relation:
            a = []
            for i in idx:
                a.append(person[i])
            lst.append(tuple(a))

        if len(set(lst)) == len(relation):
            flag = True

        for c in check:
            if set(c).issubset(idx):
                flag = False
                break

        if flag == True:
            check.append(idx)

    return len(check)


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]

print(solution(relation))
