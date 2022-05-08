import enum
from inspect import isdatadescriptor


def solution(s):
    answer = ''
    word_lst = s.split(' ')
    for i in word_lst:
        # 각 word의 길이만큼 for-loop 순회
        for j in range(len(i)):
            # word의 index가 짝수인 경우,
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]


s = "try hello world"
print(solution(s))
