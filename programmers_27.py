# arr가 주어진다. (0~9)
# 연속된 숫자는 한 개만 남기고, 제거한다.

arr = [1, 1, 3, 3, 0, 1, 1]

answer = []

prev_num = -99999
for n in arr:
    if prev_num != n:
        answer.append(n)
        prev_num = n

print(answer)


def solution(arr):
    answer = []
    prev_num = -99999
    for n in arr:
        if prev_num != n:
            answer.append(n)
            prev_num = n
    return answer

# ------------------------------

# 모범답안


def no_continuous(s):
    a = []
    print('before a[-1:]', a[-1:])
    for i in s:
        # a[-1]로 정확하게 index를 잘라내면 out of index에러가 발생하지만,
        # a[-1:]처럼 a[-1]과 동일한 효과로 slicing을 해준다면 에러가 발생하지 않는다.
        if a[-1:] == [i]:
            continue
        a.append(i)
    print('after a[-1:]', a[-1:])
    return a


print(no_continuous("133303"))
