# 점프 silver 1
# https://www.acmicpc.net/problem/1890
# 24-01-18  python3 31120 KB	40 ms

from collections import deque


# dp
def solution():
    answer = 0
    dr = [0, 1]
    dc = [1, 0]
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    for r in range(N):
        for c in range(N):
            move = board[r][c]
            if not move:
                continue
            for i in range(2):
                nr = r + dr[i] * move
                nc = c + dc[i] * move
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                dp[nr][nc] += dp[r][c]

    print(dp[N - 1][N - 1])


# bfs
def memory_exceeded():
    answer = 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1]
    dc = [1, 0]
    que = deque()
    que.append([0, 0])
    while que:
        r, c = que.popleft()
        move = board[r][c]
        if r == N - 1 and c == N - 1:
            answer += 1
            continue
        elif move == 0:
            continue
        for i in range(2):
            nr = r + dr[i] * move
            nc = c + dc[i] * move
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            que.append([nr, nc])
    print(answer)


solution()
