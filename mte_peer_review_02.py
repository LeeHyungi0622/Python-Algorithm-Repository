# 내가 처음 이 문제를 봤을때는 people, tshirts 리스트를
# 이중 for문으로 돌려서 서로 비교를 하려고 하였고,
# for문에서 사용하는 iterable 객체를 for 문내에서 처리과정에서 수정을 하면,
# for문이 중단다는 것을 배웠다.
# 그래서 for 문을 돌리는 대상 iterable 객체는 복사를 해서 해도 되지만, 
# iterable 객체는 수정하지 않으면서, 결과값만 다른 변수에 담아서 처리해야된다는 것을 배웠다.

def solution(people, tshirts):
    # 최대 나눠줄 수 있는 셔츠의 수
    answer = 0

    # people, tshirts 배열을 오름차순 정렬한다.
    people.sort()
    tshirts.sort()

    # people 배열을 순회하기 위해서 index값, i를 0으로 우선 초기화 한다.
    i = 0

    # 보유한 셔츠의 사이즈를 가지고 있는 리스트 (tshirts)를 순회한다.
    for t in tshirts:
        try:
           # 만약 people의 i번째의 값이 존재하고, people의 i 번째 수가 t(셔츠 사이즈)ㅂ
           # 보다 작으면, 셔츠를 나눠 줄 수 있는 조건에 만족하기 때문에 answer을 1증가, 
           # people 리스트 순회 index 변수 i를 증가시켜준다.
           if people[i] and people[i] <= t:
                answer += 1
                i += 1
        # 여기서 people[i]가 존재하지 않는 index일 수 있기 때문에 exception에서 
        # people 리스트를 더 이상 순회할 수 없는 경우, break하도록 처리하였다.        
        except:
            break;
    return answer