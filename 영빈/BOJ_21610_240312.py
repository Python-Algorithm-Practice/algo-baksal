# 마법사 상어와 비바라기 gold 5
# https://www.acmicpc.net/problem/21610
# 24-03-12  38968 KB	324 ms


from typing import List


def solution():
    N, M = map(int, input().split())
    clouds = [[False] * N for _ in range(N)]
    baskets = [list(map(int, input().split())) for _ in range(N)]

    def move(clouds: List[List[int]], d: int, s: int):
        dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
        dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
        new_clouds = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if not clouds[r][c]:
                    continue
                new_clouds[(r + dr[d] * s) % N][(c + dc[d] * s) % N] = True
        return new_clouds

    def rain(clouds: List[List[int]]):
        for r in range(N):
            for c in range(N):
                if not clouds[r][c]:
                    continue
                baskets[r][c] += 1
        return

    def bug(clouds: List[List[int]]):
        dr = [-1, -1, 1, 1]
        dc = [-1, 1, -1, 1]

        for r in range(N):
            for c in range(N):
                if not clouds[r][c]:
                    continue
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    baskets[r][c] += 1 if baskets[nr][nc] else 0
        return

    def cloudy(clouds: List[List[int]]):
        new_clouds = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if clouds[r][c]:
                    continue
                elif baskets[r][c] >= 2:
                    baskets[r][c] -= 2
                    new_clouds[r][c] = True
        return new_clouds

    clouds[N - 1][0] = True
    clouds[N - 1][1] = True
    clouds[N - 2][0] = True
    clouds[N - 2][1] = True
    for _ in range(M):
        d, s = map(int, input().split())
        clouds = move(clouds, d, s)
        rain(clouds)
        bug(clouds)
        clouds = cloudy(clouds)

    answer = 0
    for r in range(N):
        for c in range(N):
            answer += baskets[r][c]
    print(answer)
    return


solution()
