
N = 5
number = 12

# s = [set() for x in range(8)]

# print(s)

# for i, x in enumerate(s, start=1):
#     x.add(int(str(N) * i))

# print(s)

# for i in range(1, 8):
#     for j in range(i):
#         for op1 in s[j]:
#             for op2 in s[i-j-1]:
#                 s[i].add(op1 + op2)
#                 s[i].add(op1 - op2)
#                 s[i].add(op1 * op2)
#                 if op2 != 0:
#                     s[i].add(op1 // op2)
#     if number in s[i]:
#         answer = i + 1
#         break
# else:
#     answer = -1

# print(s)


def solution(N, number):
    if N == number:
        return 1
    answer = 0
    lst = [set() for _ in range(8)]
    
    for idx, val in enumerate(lst, start=1):
        val.add(int(str(N)*idx))

    # i: 1, j: 0, i-j-1: 0
    # i: 2, j: 0, i-j-1: 1
    # i: 2, j: 1, i-j-1: 0
    # i: 3, j: 0, i-j-1: 2
    # i: 3, j: 1, i-j-1: 1
    # i: 3, j: 2, i-j-1: 0
    # i: 4, j: 0, i-j-1: 3
    # i: 4, j: 1, i-j-1: 2
    # i: 4, j: 2, i-j-1: 1
    # i: 4, j: 3, i-j-1: 0

    for i in range(1, 8):
        for j in range(i):
            for num1 in lst[j]:
                for num2 in lst[i-j-1]:
                    if num2 is not 0:
                        lst[i].add(num1 // num2)
                    lst[i].add(num1 + num2)
                    lst[i].add(num1 - num2)
                    lst[i].add(num1 * num2)
        if number in lst[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer

        
        
    
print(solution(N, number))


def solution(N, number):
    s = [set() for x in range(8)]
    
    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))
    
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 * op2)
                    s[i].add(op1 - op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer