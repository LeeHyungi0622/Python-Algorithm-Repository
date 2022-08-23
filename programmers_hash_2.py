def solution(participant, completion):
    p_lst = {p: 0 for p in set(participant)}
    for p in participant:
        p_lst[p] += 1

    for c in completion:
        p_lst[c] -= 1

    for k, v in p_lst.items():
        if v == 1:
            return k


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))
