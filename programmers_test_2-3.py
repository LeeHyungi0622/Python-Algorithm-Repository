from collections import defaultdict


def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)

    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    print("graph::", graph)

    Q = []
    # 총 지역의 수가 n개로 주어졌기 때문에 visited(방문지역) 수 만큼 -1의 값을 갖는 리스트를 정의한다.
    visited = [-1 for _ in range(n + 1)]
    # 도착 지점은 0으로 셋팅한다. 그 이유는 도착지 부터 다른 노드까지의 거리를 산정해야 되기 때문이다.
    visited[destination] = 0
    # 현 위치(cur)와 거리(distance)를 큐에 담는다.(현 위치가 destination이면, 도착지까지의 이동거리는 0이 된다)
    Q.append([destination, 0])

    # print(visited)

    # Q(ueue)가 빌때까지 반복 처리한다.
    while Q:
        cur, dis = Q.pop(0)
        for i in graph[cur]:
            # 만약에 방문한 이력이 있는 경로인 경우, 다른 경로로 방문을 한다.
            if visited[i] >= 0:
                continue
            # 방문한 이력이 없는 경로의 경우에는
            # 해당 경로의 정보를 가진 visited index 위치에  도착지로부터 +1 더한 값을 visited 리스트에 업데이트 한다.
            # 도착지로부터 거리 업데이트
            visited[i] = dis + 1

            # 새롭게 방문하는 경로에 대해서 Queue에 쌓는다.
            Q.append([i, dis + 1])

    for source in sources:
        answer.append(visited[source])

    return answer


n = 3
roads = [[1, 2], [2, 3]]
sources = [2, 3]
destination = 1

print(solution(n, roads, sources, destination))

# t_dict = {1: {2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1}}

# for i in t_dict[2]:
#     print(i)
