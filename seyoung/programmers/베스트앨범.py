"""
Q. 베스트앨범
link: https://school.programmers.co.kr/learn/courses/30/lessons/42579
key: 해시
"""
from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []

    genre_dict = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((idx, play))

    sorted_genres = sorted(genre_dict.items(), key=lambda x: sum([p for (_, p) in x[1]]), reverse=True)
    for _, play_list in sorted_genres:
        two_largest = heapq.nlargest(2, play_list, key=lambda x: (x[1], -x[0]))
        for idx, _ in two_largest:
            answer.append(idx)

    return answer


def solution(genres, plays):
    answer = []

    genre_songs = defaultdict(list)
    genre_plays = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_songs[g].append((i, p))
        genre_plays[g] += p

    for (k, _) in sorted(genre_plays.items(), key=lambda x: x[1], reverse=True):
        for (i, _) in sorted(genre_songs[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer


if __name__ == '__main__':
    in_data = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
    res = solution(*in_data)
    print(res)  # 	[4, 1, 3, 0]

    in_data = 	["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    res = solution(*in_data)
    print(res)  # 	[0, 1, 2, 4]