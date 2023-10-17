# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 스택 사용 안함
# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

# 시간초과....
# def solution(prices):
#     answer = []
#     while prices:
#         cnt = 0
#         x = prices.pop(0)
#         for i in prices:
#             cnt+=1
#             if x > i:
#                 break
#         answer.append(cnt)

#     return answer

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        cnt = 0
        x = prices.popleft()
        for i in prices:
            cnt+=1
            if x > i:
                break
        answer.append(cnt)

    return answer