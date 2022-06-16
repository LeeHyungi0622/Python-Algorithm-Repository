# from queue import PriorityQueue

# def solution(scoville, k):
#     answer = 0
#     pq = PriorityQueue()

#     for s in scoville:
#         pq.put(s)

#     while pq.queue[0] < k and len(pq.queue) > 1:
#         pq.put(pq.get() + (pq.get()*2))
#         answer += 1
        
#     return answer if pq.queue[0] >= k else -1

# scoville = [1, 2, 3, 9, 10, 12]
# k = 7 

# print(solution(scoville, k))

from heapq import *

def solution(scoville, k):
    count = 0
    heapify(scoville)
    
    while scoville[0] < k and len(scoville) > 1:
        heappush(scoville, heappop(scoville) + (heappop(scoville) * 2))
        count += 1
    
    return count if scoville[0] >= k else -1

scoville = [1, 2, 3, 9, 10, 12]
k = 7 

print(solution(scoville, k))


