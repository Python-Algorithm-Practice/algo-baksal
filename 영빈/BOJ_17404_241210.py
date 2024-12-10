# RGB거리 2     gold 4
# https://www.acmicpc.net/problem/17404
# 24-12-10  python 3    33432 KB	60 ms


def solution():
    R = 0
    G = 1
    B = 2
    INF = 1_000_000

    answer = INF
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    for color in range(3):
        dp = [[INF] * N for _ in range(3)]
        dp[color][0] = costs[0][color]
        for i in range(1, N-1):
            dp[R][i] = costs[i][R] + min(dp[G][i-1], dp[B][i-1])
            dp[G][i] = costs[i][G] + min(dp[R][i-1], dp[B][i-1])
            dp[B][i] = costs[i][B] + min(dp[R][i-1], dp[G][i-1])
            
        if color == R:
            dp[G][N-1] = costs[N-1][G] + min(dp[R][N-2], dp[B][N-2])
            dp[B][N-1] = costs[N-1][B] + min(dp[R][N-2], dp[G][N-2])
        elif color == G:
            dp[R][N-1] = costs[N-1][R] + min(dp[G][N-2], dp[B][N-2])
            dp[B][N-1] = costs[N-1][B] + min(dp[R][N-2], dp[G][N-2])
        if color == B:
            dp[G][N-1] = costs[N-1][G] + min(dp[R][N-2], dp[B][N-2])
            dp[R][N-1] = costs[N-1][R] + min(dp[G][N-2], dp[B][N-2])
        answer = min(answer, dp[R][-1], dp[G][-1], dp[B][-1])
    return print(answer)

solution()