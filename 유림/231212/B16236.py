
""" [백준] 골드 3. 아기 상어 """

import sys
from collections import deque

def solution():
    
    input = sys.stdin.readline

    N = int(input())                # 공간의 크기

    shark = [0] * 3                 # 아기 상어의 위치
    sea = []

    for i in range(N):
        sea.append(list(map(int, input().split())))
        for j in range(N):
            if sea[i][j] == 9:
                shark[0], shark[1], shark[2] = i, j, 2
                sea[i][j] = 0
    
    return move(N, sea, shark)


def move(N, sea:list, shark:list):

    time_count = 0
    fish_count = 0

    while True:

        fish = seek_fish(N, sea, shark)

        if fish == -1:
            return time_count
        
        # 시간
        time_count += fish[2]
        
        # 물고기
        fish_count += 1
        sea[fish[0]][fish[1]] = 0

        # 상어
        shark[0], shark[1] = fish[0], fish[1]

        if fish_count == shark[2]:
            shark[2] += 1
            fish_count = 0


def seek_fish(N, sea:list, shark:list):

    dr = [-1, 0, 0, 1]      # 상좌우하
    dc = [0, -1, 1, 0]

    visited = [[False] * N for _ in range(N)]
    possible_fish = []

    q = deque()

    q.append((shark[0], shark[1], 0))
    visited[shark[0]][shark[1]] = True

    while q:

        r, c, dis = q.popleft()

        for d in range(4):

            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc] or shark[2] < sea[nr][nc]:
                continue

            if 0 < sea[nr][nc] < shark[2]:
                possible_fish.append((nr, nc, dis+1))
            
            q.append((nr, nc, dis+1))
            visited[nr][nc] = True
    
    return sorted(possible_fish, key=lambda x : (x[2], x[0], x[1]))[0] if possible_fish else -1

print(solution())
