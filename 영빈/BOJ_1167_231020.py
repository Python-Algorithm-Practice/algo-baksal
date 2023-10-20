# 트리의 지름 gold 2
# https://www.acmicpc.net/problem/1167

import sys

def find_path(cur, distance, visited):
    global adj_list
    if visited[cur]:
        return 
    
    for node, length in adj_list[cur]:
        find_path(node, distance + length, visited)
def solution():
    input = sys.stdin.readline
    V = int(input())
    adj_list = [[] for _ in range(V)]
    memo = [[0] * V for _ in range(V)]
    for _ in range(V):
        node, *info = map(int, input().strip().split())
        adj_list[node - 1] = [
            (info[i] - 1, info[i + 1]) for i in range(0, len(info) - 1, 2)
        ]

    print()


solution()
