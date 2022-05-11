# N, M = map(int, input().split(' '))

# num_lst = list(map(int, input().split(' ')))

N = 8
M = 32
num_lst = [23, 87, 65, 12, 57, 32, 99, 81]

num_lst.sort()

start = 0
end = len(num_lst) - 1
mid = len(num_lst) // 2

while start <= end:
    mid = (start + end) // 2
    if num_lst[mid] == M:
        print(mid+1)
        break
    elif num_lst[mid] > M:
        end = mid - 1
    elif num_lst[mid] < M:
        start = mid + 1
