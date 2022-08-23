def solution(clothes):
    answer = 1
    clothes_dict = {k: [] for [_, k] in clothes}

    for [v, k] in clothes:
        clothes_dict[k].append(v)

    for key in clothes_dict.keys():
        answer = answer * (len(clothes_dict[key]) + 1)

    return answer - 1


clothes = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

print(solution(clothes))

import collections
from functools import reduce


def solution1(clothes):
    print(
        reduce(
            lambda x, y: x * y,
            [a + 1 for a in collections.Counter([x[1] for x in clothes]).values()],
        )
        - 1
    )


solution1(clothes)

# return

# reduce(
#     lambda x,y:x*y,
#         [a+1
#             for a in collections.Counter([x[1] for x in c]).values()
#         ]
# )-1
