def solution(rows, columns, max_virus, queries):
    answer = []

    arr = [[0]*(columns+2) for _ in range(rows+2)]

    for x, y in queries:
        if arr[x][y] < max_virus:
            arr[x][y] += 1
        elif arr[x][y] == max_virus:
            if arr[x][y-1] < max_virus:
                arr[x][y-1] += 1
            if arr[x][y+1] < max_virus:
                arr[x][y+1] += 1
            if arr[x-1][y] < max_virus:
                arr[x-1][y] += 1
            if arr[x+1][y] < max_virus:
                arr[x+1][y] += 1
    for i in range(1, rows+1):
        answer.append(arr[i][1:columns+1])  
    return answer

rows = 3
columns = 4
max_virus = 2

queries = [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]

print(solution(rows=rows, columns=columns, max_virus=max_virus, queries=queries))