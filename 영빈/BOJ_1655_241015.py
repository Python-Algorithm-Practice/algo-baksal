# 가운데를 말해요   gold 2
# https://www.acmicpc.net/problem/1655
# 24-10-15  python 3  48552 KB	152 ms

import sys
from heapq import heapify, heappop, heappush

def solution():
    input = sys.stdin.readline
    answer = []
    N = int(input())
    left = []
    right = []
    heapify(left)
    heapify(right)
    mid = int(input())
    answer.append(mid)
    heappush(left, mid * -1)  # mid는 항상 left[0]이다.

    def find_mid(num: int):
        nonlocal mid

        if num <= mid:
            heappush(left, num * -1)
            if len(left) > len(right) + 1:
                heappush(right, heappop(left) * -1)
                mid = heappop(left) * -1
                heappush(left, mid * -1)
        elif num > mid:
            heappush(right, num)
            if len(left) < len(right):
                mid = heappop(right)
                heappush(left, mid * -1)
        return

    for _ in range(1, N):
        num = int(input())
        find_mid(num)
        answer.append(mid)
    return print('\n'.join(map(str, answer)))

solution()