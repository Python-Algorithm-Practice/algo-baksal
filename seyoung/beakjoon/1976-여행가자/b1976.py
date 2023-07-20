"""
Q. [BOJ] 1976. 여행 가자
lv. G4
link: https://www.acmicpc.net/problem/1976
key: Graph, Disjoint Set
"""


def solution():
    def find(v: int) -> int:
        if v != p[v]:
            p[v] = find(p[v])
        return p[v]

    def union(u: int, v: int):
        u = find(u)
        v = find(v)
        if u > v:
            u, v = v, u
        p[u] = v

    N, _ = int(input()), input()
    graph = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(lambda x: int(x) - 1, input().split()))

    p = [i for i in range(N + 1)]
    for i in range(N):
        for j in range(i):
            if graph[i][j]:
                union(i, j)

    answer = True
    target = find(plan[0])
    for cur in plan[1:]:
        if find(cur) != target:
            answer = False
            break
    print('YES' if answer else 'NO')


if __name__ == '__main__':
    solution()
