
""" [백준] 골드 2. 트리의 지름 """

import sys
from collections import deque

def solution():

    input = sys.stdin.readline

    V = int(input())                            # 트리의 정점 개수

    graph = [[] * (V+1) for _ in range(V+1)]    # 트리의 연결
    
    for _ in range(V):
        temp = list(map(int, input().split()))
        for idx in range(1, len(temp)-1, 2):
            graph[temp[0]].append((temp[idx], temp[idx+1]))

    idx, distance = search(graph, V, 1)         
    idx, distance = search(graph, V, idx)

    return distance

def search(graph, V, start):
    
    visited = [False] * (V+1)

    q = deque()

    q.append((start, 0))
    visited[start] = True

    idx, distance = start, 0
    
    while q:

        node, dis = q.popleft()

        if distance < dis:      # 가장 멀리 있는 거리, index 구하기
            distance = dis
            idx = node

        for (n, d) in graph[node]:
            if not visited[n]:
                visited[n] = True
                q.append((n, dis + d))
    
    return idx, distance


print(solution())