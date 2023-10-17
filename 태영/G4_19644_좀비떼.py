import sys
from collections import deque

input = sys.stdin.readline

l = int(input())
ml, mk = map(int, input().split())
c = int(input())
ll = list(int(input()) for _ in range(l))
survive = True
zombie = 0
pointer = min(l, ml)

for i in range(min(l, ml)):
    ll[i] = max(0, ll[i]-(i+1)*mk)
    print(ll)
if survive:
    if(l>ml):
        for i in range(1, l-ml+1):
            # print(ll[i+ml-1] - (i * mk))
            ll[i+ml-1] = max(0, ll[i+ml-1] - (i * mk))
            print(ll)


for i in ll:
    if i:
        c -= 1
        if c<0:
            survive = False


if survive:
    print('YES')
else: print('NO')
