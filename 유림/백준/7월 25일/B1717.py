
""" 골드 5. 집합의 표현 """

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())       # 원소 개수, 연산 개수
parent = [num for num in range(N+1)]                # 부모 테이블

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):

    check, a, b = map(int, sys.stdin.readline().split())

    if check == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")