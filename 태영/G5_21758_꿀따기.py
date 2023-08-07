import sys
from itertools import combinations


input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

total = sum(line)
honey = 0

bee = line[0]
for i in range(1, n):
    bee += line[i]
    honey = max(honey, total - line[0] - line[i] + total - bee)

bee = line[-1]
for i in range(n-2, -1, -1):
    bee += line[i]
    honey = max(honey, total - line[-1] - line[i] + total - bee)


for i in range(1, n):
    honey = max(honey, total - line[0] - line[-1] + line[i])

print(honey)

