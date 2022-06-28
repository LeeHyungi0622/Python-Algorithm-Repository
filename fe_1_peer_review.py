from collections import deque
def solution(rows, columns, max_virus, queries):
    answer = [[0] * columns for _ in range(rows)]

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    for query in queries:
        visited = [[False] * columns for _ in range(rows)]
        row, column = query
        
        x = row - 1
        y = column - 1
        if answer[x][y] == max_virus:
            queue = deque([[x,y]])  
            while queue:
                r, c = queue.popleft()
                for i in range(4):
                    R = dr[i] + r
                    C = dc[i] + c

                    if R < 0 or C < 0 or R >= rows or C >= columns:
                        continue

                    if not visited[R][C]:
                        visited[R][C] = True
                        if answer[R][C] == max_virus:
                            queue.append([R,C])
                        else:
                            answer[R][C] += 1
                
        else:
            answer[row-1][column-1] += 1

    return answer