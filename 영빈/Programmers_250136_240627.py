# [PCCP 기출문제] 2번 / 석유 시추   level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/250136
# 24-06-27  python 3


from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    lump_sizes = [0]
    lumps = [[0] * m for _ in range(n)]
    
    def find_lumps(i, j):
        nonlocal lump_sizes, lumps
        dr = [-1, 0, 0, 1]
        dc = [0, -1, 1, 0]
        num = len(lump_sizes)
        size = 1
        
        que = deque()
        que.append((i, j))
        lumps[i][j] = num
        
        while que:
            r, c = que.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nc < 0 or nr >= n or nc >= m \
                    or not land[nr][nc] or lumps[nr][nc] != 0:
                    continue
                que.append((nr, nc))
                lumps[nr][nc] = num
                size += 1
        if size > 0:
            lump_sizes.append(size)
        
    for i in range(n):
        for j in range(m):
            if land[i][j] and not lumps[i][j]:
                find_lumps(i, j)
            
    for j in range(m):
        digged_lumps = set()
        amount = 0
        for i in range(n):
            digged_lumps.add(lumps[i][j])
        for lump in digged_lumps:
            amount += lump_sizes[lump]
        answer = max(answer, amount)
    return answer