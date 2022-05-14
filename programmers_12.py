def solution(answers):
    stdnt_1_ptn = [1, 2, 3, 4, 5]
    stdnt_2_ptn = [2, 1, 2, 3, 2, 4, 2, 5]
    stdnt_3_ptn = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stdnt_1_chk = [0] * len(answers)
    stdnt_2_chk = [0] * len(answers)
    stdnt_3_chk = [0] * len(answers)

    for idx, val in enumerate(answers):
        if stdnt_1_ptn[idx % len(stdnt_1_ptn)] == val:
            stdnt_1_chk[idx] = 1

    for idx, val in enumerate(answers):
        if stdnt_2_ptn[idx % len(stdnt_2_ptn)] == val:
            stdnt_2_chk[idx] = 1

    for idx, val in enumerate(answers):
        if stdnt_3_ptn[idx % len(stdnt_3_ptn)] == val:
            stdnt_3_chk[idx] = 1

    answer_cnt = []
    answer_cnt.append(stdnt_1_chk.count(1))
    answer_cnt.append(stdnt_2_chk.count(1))
    answer_cnt.append(stdnt_3_chk.count(1))

    return [(idx+1) for idx, v in enumerate(answer_cnt) if v == max(answer_cnt)]


answers = [1, 2, 3, 4, 5]

print(solution(answers))


# ==== 모범 답안 코드(Python)

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
