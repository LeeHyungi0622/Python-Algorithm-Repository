def solution(sizes):

    left_el = []
    right_el = []
    for s in sizes:
        s.sort(reverse=True)
        left_el.append(s[0])
        right_el.append(s[1])

    return sorted(left_el, reverse=True)[0] * sorted(right_el, reverse=True)[0]


sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes))
