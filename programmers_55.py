def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):

            if prev == s[j:j+step]:
                count += 1
            else:
                # count값이 누적이 된 경우가 있을 수 있으므로, 누적된 경우에 2 이상인 경우에는
                # 아래와같은 조건분기로 압축된 string형태로 formatting을 해줘야한다.
                compressed += str(count) + prev if count >= 2 else prev
                # prev값과 그 다음 값이 같지 않은 경우에는 prev값을 그 다음 step의 값으로 업데이트한다.
                prev = s[j:j+step]
                # 그리고 count 값을 1로 초기화시킨다.
                count = 1

        compressed += str(count) + prev if count >= 2 else prev

        # 생성된 문자열 최종 비교
        answer = min(answer, len(compressed))
        # 위의 과정을 len(s) // 2 + 1의 길이만큼 반복을 하면서 가장 짧은 길이를 구한다.
    return answer


s = "xababcdcdababcdcd"

print(solution(s))
