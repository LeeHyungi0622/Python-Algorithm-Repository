import re


def solution(new_id):

    new_id = new_id.lower()

    filtered_lst = []
    allow_chars = ['-', '_', '.']
    dot_flag = False

    for s in new_id:
        if s.isdigit() or s.islower() or s in allow_chars:
            if (s == '.' and not dot_flag) or s != '.':
                filtered_lst.append(s)
            if s == '.':
                dot_flag = True
            else:
                dot_flag = False

    new_id = ''.join(filtered_lst).strip('.')

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')

    if len(new_id) <= 2:
        new_id += (3-len(new_id)) * new_id[-1]

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id))


# 부분 답안 (3번째 부분 문제 답안 풀이)
# 3 (answer 문자열에 '..'이 있는 한 계속해서 replace method로 반복해서 한개로 바꿔주기)
while '..' in answer:
    answer = answer.replace('..', '.')


# 모범답안 (정규표현식 활용해서 풀이)
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + \
        "".join([st[-1] for i in range(3-len(st))])
    return st
