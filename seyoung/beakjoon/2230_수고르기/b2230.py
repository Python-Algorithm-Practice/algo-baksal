"""
Q. [BOJ] 2230. 수 고르기
link: https://www.acmicpc.net/problem/2230

"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 시간 초과
def solution_timeout():
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    answer = arr[-1] - arr[0]
    for i in range(n):
        for x, y in zip(arr, arr[i:]):
            diff = y - x
            if m <= diff < answer:
                answer = diff
    print(answer)


def solution_timeout2():
    n, m = map(int, input().split())
    arr = set(int(input()) for _ in range(n))

    while not any(x + m in arr for x in arr):
        m += 1

    print(m)


def solution():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(int(input()) for _ in range(n))
    arr.sort()

    answer = arr[-1] - arr[0]
    l, r = 0, 1
    while l <= r:
        while r < n and arr[r] - arr[l] < m:
            r += 1
        if r < n:
            answer = min(answer, arr[r] - arr[l])
        l += 1

    print(answer)


def solution():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(int(input()) for _ in range(n))
    arr.sort()

    answer = arr[-1] - arr[0]
    l, r = 0, 0
    while r < n:
        diff = arr[r] - arr[l]
        if diff == m:
            answer = m
            break
        elif diff > m:
            if answer > diff:
                answer = diff
            l += 1
        else:
            r += 1

    print(answer)


if __name__ == "__main__":
    solution()
