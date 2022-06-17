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
