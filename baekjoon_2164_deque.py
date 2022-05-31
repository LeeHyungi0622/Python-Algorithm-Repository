from collections import deque


N = int(input())
q = deque()

for i in range(N, 0, -1):
    q.appendleft(i)

while len(q) != 1:
    q.popleft()
    next = q.popleft()
    q.append(next)

print(q[0])
