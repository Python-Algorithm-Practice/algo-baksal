
""" [프로그래머스 PCCP 모의고사 #1] 체육대회 """

import itertools

def solution(ability):
    answer = 0
    game = len(ability[0])

    npr = list(itertools.permutations(ability, game))   # 각 게임에 사람을 뽑는 경우의 수 

    for g in npr:
        count = 0
        for i in range(game):
            count += g[i][i]
        answer = max(answer, count)

    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))     # 210
print(solution([[20, 30], [30, 20], [20, 30]]))    