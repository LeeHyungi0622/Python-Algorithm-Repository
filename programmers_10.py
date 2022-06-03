def solution(participant, completion):
    p_set = set(participant)
    p_hash = {name: 0 for name in p_set}

    for n in participant:
        p_hash[n] = p_hash.get(n) + 1

    for n in completion:
        p_hash[n] = p_hash.get(n) - 1

    for k, v in p_hash.items():
        if v != 0:
            return k


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))
