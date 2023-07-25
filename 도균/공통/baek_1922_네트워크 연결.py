len_computer = int(input())
len_lines = int(input())

parents = [i for i in range(len_computer + 1)]

## 01. Union and Find
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

## 02. Sorting
lines = []
for _ in range(len_lines):
    a, b, cost = map(int, input().split())
    lines.append((cost, a, b))
lines.sort()

## 03. Kruskal
answer = 0
for line in lines:
    cost, a, b = line
    if find(a) != find(b):
        union(a, b)
        answer += cost
print(answer)