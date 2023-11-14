
""" [백준] 골드 5. 수 고르기 """

import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())        # 수열 크기 N, 차이 M
    numbers = [int(input()) for _ in range(N)]

    if N == 1 or M == 0:
        return 0

    numbers.sort()

    start, end = 0, 1
    answer = numbers[-1] - numbers[0]

    while end < len(numbers):

        diff = numbers[end] - numbers[start]

        if M <= diff:
            answer = min(answer, diff)
            start += 1
        else:
            end += 1

    return answer

print(solution())