from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()

    n = len(numbers)

    # numbers 리스트의 첫 번째 요소의 양/음의 값을 index:0으로 하여, queue에 append한다.
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    print(queue)

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
