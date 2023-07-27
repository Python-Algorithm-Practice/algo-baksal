"""
Q. [BOJ] 1922. 네트워크 연결
lv. G4
link: https://www.acmicpc.net/problem/1922
key: MST(Minimum Spanning Tree), Graph
"""

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solution():
    N = int(input())
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])

    p = [i for i in range(N + 1)]

    def find(v: int) -> int:
        if v != p[v]:
            p[v] = find(p[v])
        return p[v]

    def union(u: int, v: int) -> int:
        u = find(u)
        v = find(v)
        if u == v:
            return False
        if u < v:
            u, v = v, u
        p[u] = v
        return True

    answer = 0
    count = 0
    for a, b, c in edges:
        if union(a, b):
            answer += c
            count += 1
            if count == N - 1:
                break
    print(answer)


if __name__ == '__main__':
    solution()
