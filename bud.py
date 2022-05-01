N = int(input())

input_arr = []
for _ in range(N):
    input_arr.append(list(map(int, input().split(' '))))

# print(input_arr)

for x in input_arr:
    x.insert(0, 0)
    x.append(0)

input_arr.insert(0, [0]*(N+2))
input_arr.append([0]*(N+2))

# print(input_arr)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        # Python의 all 연산자, df
        if all(input_arr[i][j] > input_arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
            