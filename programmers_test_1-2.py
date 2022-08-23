# 100점 코드


def solution(want, number, discount):
    answer = 0
    product = dict(sorted(dict(zip(want, number)).items(), key=lambda x: x[0]))

    for i in range(0, len(discount) - 10 + 1):
        discount_dict = {p: 0 for p in set(discount[i : 10 + i])}
        for dp in discount[i : 10 + i]:
            discount_dict[dp] = discount_dict.get(dp, 0) + 1
        sorted_discount_dict = dict(sorted(discount_dict.items(), key=lambda x: x[0]))

        cnt = 0

        for k, v in product.items():
            try:
                if product[k] == sorted_discount_dict[k]:
                    cnt += 1
            except KeyError:
                pass
        if len(product) == cnt:
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]

print(solution(want, number, discount))

# product = dict(zip(want, number))

# discount_product = ["chicken", "apple", "apple"]

# print({p: 0 for p in set(discount_product)})

# product_1 = {'banana': 3, 'apple': 2, 'rice': 2, 'port': 2, 'pot': 1}
# print(sorted(product_1.items(), key=lambda x:x[0]))
