"""
Q. [BOJ] 21758. 꿀 따기
lv. G5
link: https://www.acmicpc.net/problem/21758
"""

# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# print('expected: 57 54 10')

from itertools import permutations


def solution():
    N = int(input())
    board = list(map(int, input().split()))
    answer = 0

    dp = [0 for _ in range(N)]
    for i, x in enumerate(board):
        dp[i] = x + dp[i - 1]

    def cal_honey(b, t):
        if b > t:
            b, t = b, t
        return dp[t] - dp[b]

    for bee1, bee2, target in permutations(range(N), 3):
        if bee1 > bee2: continue
        honey = cal_honey(bee1, target) + cal_honey(bee2, target)
        if bee2 < target:
            honey -= board[bee2]
        elif bee1 < target:
            honey -= board[bee1]

        answer = max(honey, answer)

    print(answer)


if __name__ == '__main__':
    solution()
