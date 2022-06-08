from collections import Counter


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


def solution(participant, completion):
    p = Counter(participant)
    # Counter({'marina': 2, 'josipa': 1, 'nikola': 1, 'vinko': 1, 'filipa': 1})
    for name in completion:
        p[name] -= 1
    return max(p, key=p.get)


print('RESULT : ', solution(participant, completion))


def solution(participant, completion):
    p = Counter(participant)
    for c in completion:
        p[c] -= 1
    return max(p, key=p.get)


print(solution(participant, completion))


def solution(participant, completion):
    # answer = ''
    completion.sort()
    participant.sort()
    completion.append(None)
    print(participant)
    print(completion)
    print('zip : ', list(zip(participant, completion)))
    for i, j in zip(participant, completion):
        if i != j:
            return i


print(solution(participant, completion))
