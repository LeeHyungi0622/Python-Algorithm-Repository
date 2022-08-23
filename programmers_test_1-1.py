def solution(X, Y):
    intersec = set(X) & set(Y)

    if len(intersec) == 0:
        return "-1"

    if len(intersec) == 1 and intersec.pop() == "0":
        return "0"

    common_x = ""
    common_y = ""

    for n in X:
        if n in intersec:
            common_x += n

    for n in Y:
        if n in intersec:
            common_y += n

    common_x = "".join(sorted(list(common_x)))
    common_y = "".join(sorted(list(common_y)))

    min_len = min(len(common_x), len(common_y))

    if len(common_x) > len(common_y):
        common_x = common_x[:min_len]
    elif len(common_x) < len(common_y):
        common_y = common_y[:min_len]

    print(common_x)
    print(common_y)

    result = ""

    if int(common_x) > int(common_y):
        result = common_x
    else:
        result = common_y

    return "".join(sorted(list(result), reverse=True))


X = "5525"
Y = "1255"

print(solution(X, Y))
