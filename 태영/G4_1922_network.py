import sys

input = sys.stdin.readline


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]


n = int(input())
m = int(input())
arr = []
parent = [i for i in range(n + 1)]
result = 0
arr = []

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

arr.sort(key=lambda x: x[2])
for a, b, cost in arr:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)




