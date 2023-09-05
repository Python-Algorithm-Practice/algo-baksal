import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
h, w, sr, sc, fr, fc = map(int, input().split())
visited = [[False]*m for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            walls.append((i, j))


def check(i, j):
    for r, c in walls:
        # print(f'{i}<={r}<{i+h} and {j} <= {c} < {j+w}')
        if i <= r < i+h and j <= c < j+w:
            return False
    return True


def bfs():
    q = deque()
    q.append((sr-1, sc-1, 0))

    while q:

        x, y, cnt = q.popleft()
        visited[x][y] = True

        if x == fr-1 and y == fc-1:
            print(cnt)

            return

        for k in range(4):

            xx = dr[k]+x
            yy = dc[k]+y

            if 0 <= xx < n and 0 <= yy < m and 0 <= xx + h - 1 < n and 0 <= yy + w - 1 < m:
                if not visited[xx][yy]:
                    if check(xx, yy):
                        visited[xx][yy] = True
                        q.append((xx, yy, cnt + 1))

    print(-1)
    return


bfs()