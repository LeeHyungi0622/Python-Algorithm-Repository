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


N = int(input())

# deque를 바로 range로 초기화시켜줄 수 있다.
dq = deque(range(1, N+1))

while len(dq) > 1:
    dq.popleft()
    # deque에서 값을 뽑고 바로 dq에 append를 해 줄 수 있다.
    dq.append(dq.popleft())

print(dq.popleft())
