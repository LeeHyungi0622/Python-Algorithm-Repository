# 이번 Peer code를 통해 배운 것은 우선 시간이 주어졌다고
# 무조건적으로 datetime을 쓰지 않아도 된다는 것. (문제 조건 제대로 이해하기)
# 그리고 10분 단위로 값을 묶을때는 10이라는 숫자로 값을 나눠서 Math.ceil을 해주면 된다는 것(0.5, 1을 동일값으로)
# 그리고 list(map(lambda x:[a, b, c])), iterable object))의 형태로 
# list와 map, lambda 함수를 적절히 조합해서 리스트를 생성해내는 방법에 대해서 
# 뭔가 우선순위로 나눠서 정렬을 할때는 [a, b, c]형태로 리스트 내 요소값을 설정해도 유용하다는 것이다.
# list.sort(key=lambda x:(x[0],-x[2]))로 하면, 
# x[0]번째 요소를 기준으로 오름차순, x[2]번째 요소를 기준으로 내림차순 정렬을 할 수 있다.

import math

def solution(booked, unbooked):
    answer = []

    # 9를 곱한 것은 모두 동일한 수로 만들기 위해 곱한 의미가 없는 수이지만,
    # 10으로 나눈 부분이 핵심인데, 5를 10으로 나눠서 Math.ceil을 해주면 0.5 -> 1이 되고,
    # 10을 10으로 나눈 값을 Math.ceil을 해주면 1 -> 1이다. 
    # 이렇게 해준 이유는 10분 단위로, 단위 수 내의 값들은 모두 같은 시간대로 처리되기 때문에
    # 정렬을 할때 고려되어야 할 대상이 안된다. 
    # 
    # 뭔가 10분단위로 같은 값을 그룹화 할때는 이 분처럼 10으로 해당 분단위 숫자를 나눠서 계산해봐야겠다.
    # 
    # 그리고 두 번째로 list, map을 사용한 부분에 대해서
    # 첫 번째 인자로 람다를 넣고, 두 번째 인자로 람다함수를 적용할 iterable한 리스트 객체를 넣었다.
    # lambda 함수는 x: [a, b, c]의 형태로 했는데, 이는 아래와 같은 출력 형태를 갖는다.
    # booked :  [[811, 'lee', True]]
    # 이는 아래에서 정렬을 할때, 
    booked = list(map(lambda x:[math.ceil(int(x[0].split(":")[0]) * 90 + int(x[0].split(":")[1]) / 10),x[1],True],booked))
    unbooked = list(map(lambda x:[math.ceil(int(x[0].split(":")[0]) * 90 + int(x[0].split(":")[1]) / 10),x[1],False],unbooked))
    
    print('booked : ', booked)
    print('unbooked : ', unbooked)

    # booked와 unbooked 리스트의 값을 answer 리스트에 다 때려박는다.
    # 예약자가 우선이므로, 값을 넣을때 예약자 정보를 우선적으로 넣는다.
    for x in booked:
        answer.append(x)
    
    for x in unbooked:
        answer.append(x)

    # booked, unbooked 값이 종합되어있는 answer 리스트를 정렬한다.
    # 정렬의 기준은 우선 0번째 인덱스 값을 기준으로 오름차순 정렬(시간이 적은 사람이 우선시 되므로)하고,
    # 두번째 인자인 예약자인지 아닌지 구분하는 flag(True or False)를 기준으로 내림차순 정렬한다. 
    # 이렇게 처리하는 이유는 우선 10분단위로 같은 값을 갖기 때문에
    # 값이 크다는 것은 일단 10분이상의 차이값을 갖는다는 의미이므로, 
    # 시간이 작은 순으로 우선 정렬을 하고, 그리고 시간이 같다면(10분 내), 세 번째 인자인 예약자 우선으로 정렬을 한다.
    print('Before sorting : ', answer)

    answer.sort(key=lambda x:(x[0],-x[2]))

    print('After sorting : ', answer)
    # return list(map(lambda x:x[1],answer))

booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]

print(solution(booked, unbooked))


list(
    map
        (
            lambda x:[
                        math.ceil(
                            int(x[0].split(":")[0]) * 90 + int(x[0].split(":")[1]) / 10
                        ), 
                        x[1], True
                     ], booked))