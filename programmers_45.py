def solution(arr):
    answer = []

    # -1을 배열에 채워서 반환하도록 처리(길이가 1이하인 경우 - 단일요소)
    if len(arr) <= 1:
        answer.append(-1)
        return answer
    else:
        del arr[arr.index(min(arr))]
        return arr


arr = [4, 3, 2, 1]

print(solution(arr))

# ===== 모범답안 (Python)

arr = [4, 3, 2, 1]


def solution(arr):
    return [i for i in arr if i > min(arr)]


print(solution(arr))
