
from collections import defaultdict


def solution(genres, plays):
    answer = []
    music_dict = defaultdict(list)
    music_sum = defaultdict(int)

    music_total_info = list(zip(genres, plays, range(len(genres))))

    for m in music_total_info:
        music_dict[m[0]].append((m[2], m[1]))
        # defaultdict(<class 'list'>, {'classic': [(3, 800), (0, 500), (2, 150)], 'pop': [(4, 2500), (1, 600)]})

    for k, v in music_dict.items():
        v.sort(key=lambda x: x[1], reverse=True)
        music_sum[k] = sum(list(item[1] for item in v))
        # defaultdict(<class 'int'>, {'classic': 1450, 'pop': 3100})

    sorted_music_dict = {
        k: v
        for k, v in sorted(music_sum.items(), key=lambda item: item[1], reverse=True)
    }

    print(sorted_music_dict.keys())
    # dict_keys(['pop', 'classic'])

    for k in sorted_music_dict.keys():
        cnt = 0
        for item in music_dict[k]:
            answer.append(item[0])
            cnt += 1
            if cnt == 2:
                break

    return answer


genres, plays = ["classic", "pop", "classic", "classic", "pop"], [
    500,
    600,
    150,
    800,
    2500,
]

print(solution(genres, plays))


# genres_w_idx = [(idx, g) for idx, g in enumerate(genres)]

# print(list(zip(genres_w_idx, plays)))


# values = [(0, 500), (2, 150)]

# print(list(sum(item[i] for item in values) for i in range(len(values)))[1])
