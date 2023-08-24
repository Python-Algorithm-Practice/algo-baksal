# 베스트앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 23-08-18

from collections import defaultdict


def solution(genres, plays):
    answer = []
    play_per_genre = defaultdict(int)  # key: 장르, value: 장르가 재생된 횟수
    music_in_genre = defaultdict(list)  # key: 장르, value: 장르에 속하는 음악 고유 번호
    for num in range(len(genres)):
        play_per_genre[genres[num]] += plays[num]
        music_in_genre[genres[num]].append((plays[num], num))
    sorted_genre = sorted(play_per_genre.items(), key=lambda x: x[1], reverse=True)
    for genre, _ in sorted_genre:
        music_in_genre[genre].sort(key=lambda x: (x[0] * -1, x[1]))
        answer.append(music_in_genre[genre][0][1])
        if len(music_in_genre[genre]) > 1:
            answer.append(music_in_genre[genre][1][1])
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
