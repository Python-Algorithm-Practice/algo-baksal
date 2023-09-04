# 열쇠 gold 1
# https://www.acmicpc.net/problem/9328
# 23-09-05  python3 38504 KB	444 ms
#           pypy3   128808 KB	392 ms

from collections import deque
import sys
from typing import List, Set, Tuple


def bfs(
    entrances: List[List[int]],
    keys: Set[str],
    docs: Set[Tuple[int]],
    building: List[List[str]],
):
    def is_ouside(r: int, c: int):  # boundary 조건 확인
        if r < 0 or r >= len(building) or c < 0 or c >= len(building[0]):
            return True
        return False

    def can_pass(r: int, c: int):  # 지나갈 수 있는지 확인
        nonlocal getNewKey
        if building[r][c] == "*":
            return False
        elif building[r][c].isupper() and building[r][c].lower() not in keys:
            return False
        elif building[r][c].islower() and building[r][c] not in keys:
            getNewKey = True
            keys.add(building[r][c])
        elif building[r][c] == "$":
            docs.add((r, c))
        return True

    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    visited = [[False] * len(building[0]) for _ in range(len(building))]
    getNewKey = False
    for ent in entrances:
        # 들어갈 수 있는 입구인지 확인
        if not can_pass(ent[0], ent[1]):
            continue
        que = deque()
        que.append(ent)
        visited[ent[0]][ent[1]] = True
        while que:
            r, c = que.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if is_ouside(nr, nc) or visited[nr][nc] or not can_pass(nr, nc):
                    continue
                que.append([nr, nc])
                visited[nr][nc] = True
    return keys, getNewKey, docs


def solution():
    # 0. input 받기
    input = sys.stdin.readline
    tc = int(input())
    for _ in range(tc):
        h, w = map(int, input().split())
        building = [list(input().strip()) for _ in range(h)]
        keystring = list(input().strip())

        # 1. 입구 찾기
        entrances = []
        for r in range(h):
            if building[r][0] != "*":
                entrances.append([r, 0])
            if building[r][w - 1] != "*":
                entrances.append([r, w - 1])
        for c in range(1, w - 1):
            if building[0][c] != "*":
                entrances.append([0, c])
            if building[h - 1][c] != "*":
                entrances.append([h - 1, c])

        # 2. 열쇠와 문서 모으기: bfs
        keys = set()
        docs = set()
        if keystring[0] != "0":
            for key in keystring:
                keys.add(key)
        getNewKey = True
        while getNewKey:
            getNewKey = False
            keys, getNewKey, docs = bfs(entrances, keys, docs, building)
        print(len(docs))


solution()
