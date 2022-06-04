# from itertools import combinations


# def solution(number, k):
#     comb_lst = list(combinations(number, len(number) - k))
#     return str(max([int(''.join(list(tu))) for tu in comb_lst]))


# number = "4177252841"

# k = 4

# print(solution(number, k))

def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        # 들어오는 값이 기존 스택에 있는 값보다 크고, 빼려는 횟수 k가 아직 남아있는 경우,
        # 작으면 위에 쌓을 수 있지만, 크면 위에 못 쌓는다.
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
        print(stack)
    # k가 주어진 갯수만큼 빠졌으면 0이 되기 때문에 해당 배열의 요소를 문자열로 합쳐주면 된다.
    # 다만, k 만큼 빠지지 않았다면, 맨 뒤에서 빠지지 않은 수 만큼 잘라서 stack배열을 slicing하고, 그 요소들을 문자열로 조인해준다.
    return ''.join(stack) if k == 0 else "".join(stack[:-k])


number = "4177252841"
k = 4
print(solution(number, 4))
