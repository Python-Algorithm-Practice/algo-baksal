"""
끄루스깔
"""
import sys


def find_parent(parents, idx):
    if parents[idx] != idx:
        parents[idx] = find_parent(parents, parents[idx])
    return parents[idx]


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    m = int(sys_input())

    # 경로별 최소비용 구하기
    path_to_cost = dict()
    for _ in range(m):
        a, b, c = map(int, sys_input().split())
        key = (min(a, b), max(a, b))

        # 존재하던 경로면 최솟값 갱신, 아니면 새로 삽입
        if key in path_to_cost:
            path_to_cost[key] = min(c, path_to_cost[key])
        else:
            path_to_cost[key] = c

    # 비용 기준 오름차순 정렬
    edges = sorted((cost, a, b) for (a, b), cost in path_to_cost.items())
    parents = [i for i in range(n + 1)]
    result = 0

    # 경로를 돌며 다른 그룹인 경우 합치기
    for value, a, b in edges:
        a_parent = find_parent(parents, a)
        b_parent = find_parent(parents, b)
        if a_parent == b_parent:
            continue
        result += value
        parents[a_parent] = b_parent

    print(result)


solution()
