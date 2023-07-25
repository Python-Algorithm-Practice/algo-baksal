
""" 골드 4. 여행 가자 """

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())    # 도시 수
M = int(input())    # 여행 계획에 속한 도시들의 수

parent = [num for num in range(N)]      

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))
root = find(parent, plan[0]-1)

for city in plan[1:]:
    if find(parent, city-1) != root:
        print("NO")
        break

else:
    print("YES")