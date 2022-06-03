def solution(numbers):
    num_lst = [str(num) for num in numbers]
    num_lst.sort(key=lambda a: a*3, reverse=True)
    return str(int(''.join(num_lst)))


numbers = [3, 30, 34, 5, 9]

print(solution(numbers))
