# 특정한 최단 경로  gold 4
# https://www.acmicpc.net/problem/1504
# 24-08-13  Python3 69608 KB	460 ms
#           Pypy3   135636 KB	412 ms

import sys
from typing import List
from heapq import heappush, heappop


def dijkstra(start: int, adj_list: List[int]) -> List[int]:
    distance = [10e9] * (len(adj_list) + 1)
    distance[start] = 0
    hq = [(0, start)]
    while hq:
        dist, cur = heappop(hq)
        if distance[cur] < dist: continue
        for n, d in adj_list[cur]:
            if distance[n] <= distance[cur] + d:
                continue
            distance[n] = distance[cur] + d
            heappush(hq, (distance[n], n))
    return distance

def solution():
    input = sys.stdin.readline
    N, E = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))
    v1, v2 = map(int, input().split())

    start_dist = dijkstra(1, adj_list)
    v1_dist = dijkstra(v1, adj_list)
    dest_dist = dijkstra(N, adj_list)

    min_dist = min(start_dist[v1] + v1_dist[v2] + dest_dist[v2], start_dist[v2] + v1_dist[v2] + dest_dist[v1])
    if min_dist >= 10e9:
        return print(-1)
    print(min_dist)

solution()