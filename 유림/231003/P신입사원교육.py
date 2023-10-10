
""" [프로그래머스 PCCP 모의고사 #2] 신입사원 교육 """

import heapq

def solution(ability, number):

    q = []
    for a in ability:
        heapq.heappush(q, a)

    for _ in range(number):

        total = 0
        for _ in range(2):
            total += heapq.heappop(q)
        
        heapq.heappush(q, total)
        heapq.heappush(q, total)

    return sum(q)

print(solution([10, 3, 7, 2], 2))       # 37
print(solution([1, 2, 3, 4], 3))        # 26