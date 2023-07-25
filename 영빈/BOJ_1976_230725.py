# 여행 가자 gold 4
# https://www.acmicpc.net/problem/1976
# 23-07-25  unionfind    31256 KB	56 ms


def solution():
    N = int(input())
    M = int(input())
    parents = [i for i in range(N + 1)]

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        if parent_a < parent_b:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b

    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            if arr[j]:
                union(i + 1, j + 1)
    plan = set(map(int, input().split()))
    regions = [set() for _ in range(N + 1)]
    for i in range(1, N + 1):
        regions[find(i)].add(i)
    for i in range(1, N + 1):
        if plan - regions[i]:
            continue
        print("YES")
        return
    print("NO")


solution()
