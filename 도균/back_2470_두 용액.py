## back_2470_두 용액
## https://www.acmicpc.net/problem/2470

import sys
input = sys.stdin.readline

## 00. input
len_liq = int(input())
liq = list(map(int, input().split()))

## 01. sort : 100,000 x 8 = 800,000
liq = sorted(liq)

## 02. left ~ right
left, right = 0, len_liq - 1
now = abs(liq[left] + liq[right])
tot = [(now, liq[left], liq[right])]

while True:
    if right - left == 1:
        tot.sort()
        break

    ### 02-1. left + 1
    A = abs(liq[left + 1] + liq[right])

    ### 02-2. right - 1
    B = abs(liq[left] + liq[right - 1])

    if A < B:
        left = left + 1
        tot.append((A, liq[left], liq[right]))
    else:
        right = right - 1
        tot.append((B, liq[left], liq[right]))

## 03. answer
print(tot[0][1], tot[0][2])