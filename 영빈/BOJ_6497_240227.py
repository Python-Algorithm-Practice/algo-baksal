# 전력난 gold 4
# https://www.acmicpc.net/problem/6497
# 24-02-27  72156 KB	1268 ms
#           213180 KB	732 ms

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

answer = []


def solution():
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        return False
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])
    saved = 0
    for i in range(n):
        saved += edges[i][2]
    parents = [i for i in range(m)]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:  # cycle 검출
            return False
        parents[root_a] = min(root_a, root_b)
        parents[root_b] = min(root_a, root_b)
        return True

    def find(a):
        if parents[a] == a:
            return a
        parents[a] = find(parents[a])
        return parents[a]

    for x, y, z in edges:
        if union(x, y):
            saved -= z

    answer.append(str(saved))
    return True


while solution():
    continue

print("\n".join(answer))
