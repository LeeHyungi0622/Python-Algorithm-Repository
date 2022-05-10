# 해설강의 코드 (내가 작성한 코드의 결과값이 이상하게 나와서 일단 해설강의에서 작성한 코드로 대체)

arr = [
    [2, 4, 1, 5, 3, 2, 6],
    [3, 5, 1, 8, 7, 1, 7],
    [8, 3, 2, 7, 1, 3, 8],
    [6, 1, 2, 3, 2, 1, 1],
    [1, 3, 1, 3, 5, 3, 2],
    [1, 1, 2, 5, 6, 5, 2],
    [1, 2, 2, 2, 2, 1, 5]
]

cnt = 0

for i in range(3):
    for j in range(7):
        # 행이 j부터 i:i+5까지 슬라이스(열)
        tmp = arr[j][i:i+5]
        #  역순으로 만들어서 비교해서 같으면 회문이다.
        if tmp == tmp[::-1]:
            cnt += 1
        # 5개이기때문에 5//2 2번까지만 비교하면 된다.
        for k in range(2):
            # 세로방향으로 양 사이드의 값을 비교한다.
            if arr[i+k][j] != arr[i+5-k-1][j]:
                break
        else:
            # 정상적으로 끝나면 회문이기때문에 cnt를 증가시킨다.
            cnt += 1

print(cnt)

# 내가 작성한 코드 (결과값이 다른데 다시 한 번 풀어보기)


def judge_palindrome(arr):
    if len(arr) <= 1:
        return True
    return judge_palindrome(arr[1:-2])


N = 7

cnt = 0
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input().split(' '))))

arr = [
    [2, 4, 1, 5, 3, 2, 6],
    [3, 5, 1, 8, 7, 1, 7],
    [8, 3, 2, 7, 1, 3, 8],
    [6, 1, 2, 3, 2, 1, 1],
    [1, 3, 1, 3, 5, 3, 2],
    [1, 1, 2, 5, 6, 5, 2],
    [1, 2, 2, 2, 2, 1, 5]
]

for i in range(N):
    row = []
    col = []
    for j in range(N):
        row.append(arr[i][j])
        col.append(arr[j][i])
    print('row : ', row)
    print('col : ', col)
for k in range(3):
    if judge_palindrome(row[k:k+5]):
        cnt += 1
    if judge_palindrome(col[k:k+5]):
        cnt += 1
print(cnt)
