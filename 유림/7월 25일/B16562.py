
""" 골드 4. 친구비 """

N, M, K = map(int, input().split())             # 학생 수, 친구관계 수, 가지고 있는 돈
Fee = [0] + list(map(int, input().split()))     # 각 학생이 원하는 친구비

parent = [num for num in range(N+1)]            # 부모 테이블

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
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N+1):
    find(i)

friend = [0] * (N+1)     # 친구

for i in range(1, N+1):
    temp = find(i)
    if friend[temp] == 0:
        friend[temp] = Fee[temp]
    else:
        friend[temp] = min(friend[temp], Fee[i])
    
answer = sum(friend)

if answer <= K:
    print(answer)
else:
    print("Oh no")