def solution(order):
    answer = 0
    stack = []
    boxes = sorted(order)

    while True:
        if len(order) != 0 or len(boxes) != 0:
            if order and boxes:
                if order[0] == boxes[0]:
                    order.pop(0)
            else:
                if boxes:
                    stack.append(boxes.pop(0))
                else:
                    if stack:
                        if stack[-1] == order[0]:
                            stack.pop()
                            order.pop(0)
        else:
            return answer


order = [4, 3, 1, 2, 5]

# print(order)

print(solution(order))
