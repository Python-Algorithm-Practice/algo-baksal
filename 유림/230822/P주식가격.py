
""" [프로그래머스] Level 2. 주식가격 """

from collections import deque

def solution(prices):

    answer = []
    queue = deque(prices)

    while queue:

        price = queue.popleft()

        sum = 0
        for p in queue:
            sum += 1
            if p < price:break

        answer.append(sum)

    return answer


print(solution([1, 2, 3, 2, 3]))        # [4, 3, 1, 1, 0]