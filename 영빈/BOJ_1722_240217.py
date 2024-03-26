# 순열의 순서 gold 5
# https://www.acmicpc.net/problem/1722
# 24-02-20  40980 KB	160 ms

import math
from typing import List


def prob_1(N: int, k: int):
    seq = []
    used = [0] * (N + 1)
    used[0] = 1
    k -= 1
    for n in range(N - 1, 1, -1):
        fac = math.factorial(n)
        candid = k // fac
        elem = candid + 1
        while used[elem] or candid + sum(used[:elem]) > elem:
            elem += 1
        seq.append(elem)
        used[elem] = 1
        k %= fac
    for idx in range(N + 1):
        if not used[idx]:
            seq.append(idx)
    print(*seq)
    return


def prob_2(N: int, seq: List[int]):
    answer = 0
    used = [0] * (N + 1)
    for idx in range(N):
        used[seq[idx]] = 1
        used_num = sum(used[: seq[idx]]) + 1
        answer += (seq[idx] - used_num) * math.factorial(N - 1 - idx)
    print(answer + 1)
    return


def solution():
    N = int(input())
    prob_no, *arr = map(int, input().split())
    if prob_no == 1:
        prob_1(N, arr[0])
    elif prob_no == 2:
        prob_2(N, arr)
    return


solution()

# 5
# 1 118
# print:    5 4 3 1 2
# ans:      5 4 2 3 1
