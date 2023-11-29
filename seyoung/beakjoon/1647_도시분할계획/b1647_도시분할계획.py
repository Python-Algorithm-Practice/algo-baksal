"""
Q. [BOJ] 1647. 도시 분할 계획
lv. G4
link: https://www.acmicpc.net/problem/1647
---
크루스칼 MST 알고리즘
"""
import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    graph = list(tuple(map(int, input().split())) for _ in range(M))
    graph.sort(key=lambda x: x[2])      # 가중치 기준으로 정렬

    parents = [i for i in range(N + 1)]

    def find(v):
        if parents[v] != v:
            parents[v] = find(parents[v])
        return parents[v]

    def union(u, v):
        u = find(u)
        v = find(v)
        if u > v:
            u, v = v, u
        parents[u] = v

    total_cost = 0
    number_of_edges = 0
    for u, v, w in graph:
        if number_of_edges == N - 2:    # 마을을 분리하기 위해 마지막 마을 제외하고 연결
            break

        if find(u) != find(v):
            union(u, v)
            total_cost += w
            number_of_edges += 1

    print(total_cost)


if __name__ == "__main__":
    solution()

