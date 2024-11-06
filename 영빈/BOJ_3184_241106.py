# 양    silver 1
# https://www.acmicpc.net/submit/3184
# 24-11-06  python 3    34112 KB	100 ms


from collections import deque


def solution(): 
    R, C = map(int, input().split())
    yard = [list(input()) for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    
    def bfs(r: int, c: int):
        sheep, wolves = 0, 0
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        que = deque()
        visited[r][c] = True
        if yard[r][c] == "o":
            sheep += 1
        elif yard[r][c] == "v":
            wolves += 1
        que.append((r, c))

        while que:
            r, c = que.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                if nr < 0 or nr >= R or nc < 0 or nc >= C\
                    or visited[nr][nc] or yard[nr][nc] == "#":
                    continue
                elif nr == 0 or nr == R - 1 or nc == 0 or nc == C - 1:
                    return 0, 0
                
                visited[nr][nc] = True
                if yard[nr][nc] == "o":
                    sheep += 1
                elif yard[nr][nc] == "v":
                    wolves += 1
                que.append((nr, nc))

        return (sheep, 0) if sheep > wolves else (0, wolves)
    
    sheep, wolves = 0, 0
    for r in range(1, R):
        for c in range(1, C):
            if yard[r][c] != "#" and not visited[r][c]:
                cnts = bfs(r, c)
                sheep += cnts[0]
                wolves += cnts[1]
    return print(sheep, wolves)

solution()