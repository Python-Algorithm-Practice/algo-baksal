
""" [프로그래머스] Level 3. 베스트앨범 """

from collections import defaultdict

def solution(genres, plays):

    answer = []

    Music = defaultdict(lambda: [0])

    for idx, (genre, play) in enumerate(zip(genres, plays)):

        Music[genre][0] += play
        Music[genre].append((play, idx))

    Music = sorted(Music.items(), key=lambda x: x[1][0], reverse=True)

    for music in Music:
        
        temp = sorted(music[1][1:], key=lambda x:(-x[0], x[1]))

        answer.append(temp[0][1])
        if len(temp) > 1: 
            answer.append(temp[1][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))    # [4, 1, 3, 0]

print(solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800]))                 # [3, 0, 1]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 150, 2500]))    # [4, 1, 0, 2]