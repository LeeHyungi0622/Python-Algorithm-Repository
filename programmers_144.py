from itertools import chain
from collections import deque

def solution(tickets):
    answer = []
    dq = deque()
    dq.append('ICN')
    ticket_dict = {c: [] for c in list(set(chain(*tickets)))}


    for ticket in sorted(tickets, key=lambda x:x[1]):
        ticket_dict.get(ticket[0]).append(ticket[1])

    while dq:
        now = dq.popleft()
        answer.append(now)
        if ticket_dict.get(now):
            lst = []
            for t in ticket_dict.get(now):
                if len(ticket_dict[t]) > 0:
                    dq.append(t)
                    ticket_dict.get(now).remove(t)
                    break
                else:
                    lst.append(t)
            else:
                for t in lst:
                    answer.append(t)

    return answer

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]

tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"]

print(solution(tickets))


# 강사님 풀이 방법 
# 알파벳의 역순으로 정렬을 하는 것이 좋다. (리스트를 뒤에서부터 탐색하는 것이 효율적이다.)

def solution(tickets):
    routes = {}
    for t in tickets:
        # 리스트 병합으로 풀이 [] + []
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    
    while len(stack) > 0:
        top = stack[-1]
        # 갈수있는 공항이 없다면 (표가 없는 경우)
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        # 갈 수 있는 공항이 있다면,
        else:
            # 역순으로 정렬을 했기 때문에 제일 앞서는 공항을 스택에 넣고,
            stack.append(routes[top][-1])
            # 위의 스택에 넣은 것을 떼어낸다. (pop으로 대체 가능)
            routes[top] = routes[top][:-1]
    return path[::-1]

    