def solution(numbers):
    num_lst = [str(num) for num in numbers]
    num_lst.sort(key=lambda a: a*3, reverse=True)
    return str(int(''.join(num_lst)))


numbers = [3, 30, 34, 5, 9]

print(solution(numbers))

# 프로그래머스 강사님 코드


def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 이 부분은 숫자로 한 번 다시 바꾼다음에 문자열로 반환해도 될 것 같음
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers]
    return answer
