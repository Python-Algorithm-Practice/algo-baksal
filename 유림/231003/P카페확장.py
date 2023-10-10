
""" [프로그래머스 PCCP 모의고사 #2] 카페 확장 """

import heapq

def solution(menu, order, k):
    
    answer = 1
    start, end = -k, 0

    queue = []

    for idx in range(len(order)):

        start += k 
        end = (start if end < start else end) + menu[order[idx]]
        heapq.heappush(queue, end)

        while queue:
            now = heapq.heappop(queue)
            if start < now:
                heapq.heappush(queue, now)
                break
        
        answer = max(answer, len(queue))

    return answer


print(solution([5, 12, 30], [1, 2, 0, 1], 10))                  # 3
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))         # 4
print(solution([5], [0, 0, 0, 0, 0], 5))                        # 1

print(solution([5, 6, 7, 11], [1, 2, 3, 3, 2, 1, 1], 10))       # 2