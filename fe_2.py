from collections import deque

def check_dict(node_dict, check_elem):
    return node_dict.get(check_elem) 

def solution(s1, s2, k):
    dq = deque()
    dq.append(k)    
    answer = deque()

    node_dict = {s: [] for s in list(set(s2))}
    for p, c in zip(s1, s2):
        node_dict.get(c, []).append(p)
    print(node_dict)

    while dq:

        check_elem = dq.popleft()
        answer.appendleft(check_elem)

        check_result = node_dict[check_elem]

        for ps in sorted(check_result, reverse=True):
            cr = deque()
            while check_result:
                pv = check_r
                dq.append(ps)
        node_dict[ps]

    print(dq)
    return answer


s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]

s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]

k = "B"

solution(s1, s2, k)