"""
Q. [BOJ] 2133. 타일 채우기
lv. G4
link: https://www.acmicpc.net/problem/2133
"""


def solution():
    n = int(input())
    if n % 2:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    prev_sum = 1
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * dp[2] + prev_sum * 2
        prev_sum += dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    res = solution()
    print(res)
