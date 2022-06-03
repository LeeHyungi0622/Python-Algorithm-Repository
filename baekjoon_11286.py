import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())

pq = []

for _ in range(N):
    ip = int(input())
    if ip != 0:
        # 튜플 자료형을 담은 리스트를 정렬해서 최소 heap 값이 최종적으로 최 상단 노드로 올라가도록 설정
        # (절대값, 원본 값) 튜플형 값을 heap에 넣는다.
        hq.heappush(pq, (abs(ip), ip))
    else:
        print(hq.heappop(pq)[1] if pq else 0)

# 튜플 자료형 값을 담은 리스트를 정렬하게 되면, (x1, x2)에서 x1이 같을 경우, x2의 값을 비교한다.
# 위의 컨셉을 사용해서 이번 heap을 활용한 문제를 풀도록 한다.
arr = [(3, 4), (3, 1), (8, 5)]

# Solution2)

input = sys.stdin.readline
min_heap = []  # 양수는 절대값이 작으면 원본값도 작다. (1, 2, 5, 7, 9) - 양수 보관
max_heap = []  # 음수는 절대값이 작을수록 원본값의 비교크기가 크다. (-1, -2, -5, -7, -9) - 음수 보관

for _ in range(int(input())):
    x = int(input())

    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)
