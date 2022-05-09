def solution(s, n):
    # 입력받은 s를 리스트화 시키고,
    # 각 요소를 순회하면서 ord()로 숫자로 ASCII 값으로 변환 후에 n 값을 더한 뒤에
    # chr()로 문자로 변환해서 다시 원래 자리로 넣는다.
    # ''.join으로 문자열로 만들어서 합친다.
    lst_s = list(s)
    for idx, s in enumerate(lst_s):
        if s.isalpha():
            # 총 합계(ord(s) + n)가 ord('Z')나 ord('z')를 넘는 경우,
            # 만약에 s.islower()이면, ord('a')에 ord(s)+n - ord('z')을 더해주고,
            # 그 반대(s.isupper()이면, ord('A')에 ord(s)+n - ord('Z')를 더해준다.
            if s.islower() and (ord(s) + n > ord('z')) or s.isupper() and (ord(s) + n > ord('Z')):
                if s.islower():
                    lst_s[idx] = chr(ord('a') + ((ord(s) + n) - ord('z') - 1))
                elif s.isupper():
                    lst_s[idx] = chr(ord('A') + ((ord(s) + n) - ord('Z') - 1))
            else:
                # 그 이외의 경우에는 아래의 경우를 적용한다.
                lst_s[idx] = chr(ord(s) + n)
    return ''.join(lst_s)


s = "a B z"
n = 4

print(solution(s, n))

# ===== 모범답안(Python)

s = "b"
n = 1


def solution(s, n):
    s = list(s)
    print(s)
    for i in range(len(s)):
        if s[i].isupper():
            # 아무리 'Z'나 'z'범위를 초과하여도 나머지 연산자를 사용해서 26으로 나눠주면, 0부터 25까지
            # 범위의 나머지 값을 갖는다. 이렇게 구한 나머지 값을 ord('A') 혹은 ord('a')의 값과 합해준다.
            s[i] = chr((ord(s[i])-ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a') + n) % 26 + ord('a'))

    return "".join(s)


# 실행을 위한 테스트코드입니다.
print(solution(s, n))
