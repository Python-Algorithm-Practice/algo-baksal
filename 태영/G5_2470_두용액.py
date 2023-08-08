import sys
from itertools import combinations


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

right = n-1
left = 0


# 시간초과
# result = 1000000001
#
# dict = {}
# comb = list(combinations(arr, 2))
#
# for i, j in comb:
#     result = abs(i+j)
#     dict[result] = [i, j]
#
# dict1 = sorted(dict.items())
#
# print(*dict1[0][1])

