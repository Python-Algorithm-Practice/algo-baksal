"""
Q. [BOJ] 1922. 네트워크 연결
lv. G4
link: https://www.acmicpc.net/problem/1922
key: MST(Minimum Spanning Tree), Graph
"""

import heapq
from collections import defaultdict


def solution():
    N = int(input())
    M = int(input())

    cost_dict = defaultdict(list)
    for _ in range(M):
        a, b, c = map(int, input().split())
        cost_dict[a].append((b, c))
        cost_dict[b].append((a, c))

    answer = 0
    hq = [(0, 1)]
    visited = [False for _ in range(N + 1)]
    count = 0
    while hq and count < N:
        weight, cur = heapq.heappop(hq)
        if visited[cur]:
            continue

        count += 1
        visited[cur] += 1
        answer += weight
        for adj, c in cost_dict[cur]:
            if visited[adj]: continue
            heapq.heappush(hq, (c, adj))

    print(answer)


if __name__ == '__main__':
    solution()
