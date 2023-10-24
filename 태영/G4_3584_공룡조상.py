import sys


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    pc = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        pc[b] = a
    p, c = map(int, input().split())

    a_parent = [p]
    b_parent = [c]


