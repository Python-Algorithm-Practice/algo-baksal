"""
DP
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())

    memo = [0] * (n + 1)
    memo[0] = 1

    if n >= 2:
        memo[2] = 3

    for i in range(4, n + 1):
        # 홀수 컽
        if n % 2 == 1:
            continue

        # 2칸 당 3가지의 경우의수가 생기므로, (2칸 전 경우의수) * 3
        memo[i] = memo[i - 2] * 3

        # 4칸, 6칸, 8칸씩 걸치는 경우의수 반영하기
        # e.g. n = 10, (2칸, 8칸) (2칸, 2칸, 6칸) (2칸, 2칸, 2칸, 4칸)
        for j in range(i, 2, -2):
            memo[i] += memo[i - j] * 2

    print(memo[n])


solution()
