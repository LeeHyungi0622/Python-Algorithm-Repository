def solution(id_list, report, k):
    answer = []

    report_lst = []
    for i in report:
        report_lst.append(i.split(' '))

    report_dict = dict([(key, []) for key in id_list])

    for i in report_lst:
        if not i[1] in report_dict[i[0]]:
            report_dict[i[0]].append(i[1])

    reported_person_lst = []
    for _, v in report_dict.items():
        reported_person_lst.append(v)

    reported_person_lst_flatten = sum(reported_person_lst, [])

    reported_person_num = dict()

    for item in reported_person_lst_flatten:
        reported_person_num[item] = reported_person_num.get(item, 0) + 1

    confirmed_person = []
    for name, v in reported_person_num.items():
        if v >= k:
            confirmed_person.append(name)

    for k, v in report_dict.items():
        if v == confirmed_person:
            answer.append(len(confirmed_person))
        elif bool(set(confirmed_person).intersection(set(v))):
            answer.append(len(set(confirmed_person).intersection(set(v))))
        else:
            answer.append(0)

    return answer


# ==============================================================

# 모범 답안 (사고의 전환이 필요하다) 사고의 전환 -> 시간단축

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
