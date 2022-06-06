def solution(n, lost, reserve):
    # 여분의 체육복을 가지고 있는데, 체육복을 잃어버린 사람의 경우에는 아무 소용이 없는 사람이기 때문에
    # 처음부터 lost와 reserve 배열에서 제거하고 시작한다. 제거를 하기 위해서는 set 자료형에서 lost와 reserve의 공통값을 추출하여
    # 공통값을 각 각의 배열에서 빼준다.(차집합)
    lost = set(lost)
    reserve = set(reserve)
    result = lost.intersection(reserve)
    lost = lost - result
    reserve = reserve - result

    for i in range(1, n+1):
        if i in lost:
            if i == 1:
                if (i+1) in reserve:
                    lost.remove(i)
                    reserve.remove(i+1)
            elif i == n:
                if (n-1) in reserve:
                    lost.remove(i)
                    reserve.remove(n-1)
            else:
                if (i-1) in reserve:
                    lost.remove(i)
                    reserve.remove(i-1)
                elif (i+1) in reserve:
                    lost.remove(i)
                    reserve.remove(i+1)
    return n-len(lost)


n = 5
lost = [1, 2, 4]
reserve = [2, 3, 4, 5]

print(solution(n, lost, reserve))

n = 5
lost = [1, 2, 4]
reserve = [2, 4, 5]


# ====== 프로그래머스 커뮤러닝 강사님 풀ㅣ
def solution(n, lost, reserve):
    u = [1] * (n+2)

    for i in reserve:
        u[i] += 1

    for j in lost:
        u[j] -= 1

    for k in range(1, n+1):
        if u[k-1] == 0 and u[k] == 2:
            u[k-1:k+1] = [1, 1]
        elif u[k] == 2 and u[k+1] == 0:
            u[k:k+2] = [1, 1]
    print('result (u) : ', u)
    return len([i for i in u[1:-1] if i > 0])


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print('체육 수업을 들을 수 있는 학생 수 : ', solution(n, lost, reserve))

# ====== 모범답안 코드(Python)


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
