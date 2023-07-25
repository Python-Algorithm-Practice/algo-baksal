# 네트워크 연결 gold 4
# https://www.acmicpc.net/problem/1922
# 23-07-25  54084 KB	4340 ms


def solution():
    answer = 0
    N = int(input())
    M = int(input())
    parents = [i for i in range(N + 1)]
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])

    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        if parent_a == parent_b:
            return False
        elif parent_a < parent_b:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b
        return True

    for i in range(M):
        a, b, c = edges[i]
        if union(a, b):
            answer += c

    print(answer)


solution()
