# 좀비 떼가 기관총 진지에도 오다니 gold 4
# https://www.acmicpc.net/problem/19644
# 23-08-28

import math
import sys


def solution():
    # 0. input 받기
    input = sys.stdin.readline
    L = int(input())
    Ml, Mk = map(int, input().split())
    Cammo = int(input())
    Z = [int(input()) for _ in range(L)]

    # 1.
    used = 0
    recently_used = 0
    for idx in range(L):
        if Z[idx] > (min(idx + 1, Ml) - math.ceil(recently_used / Ml)) * Mk:
            used += 1
            recently_used += Ml
            if Cammo < used:
                print("NO")
                return
        if recently_used > 0:
            recently_used -= 1
    print("YES")


def wrong_solution():
    # 0. input 받기
    input = sys.stdin.readline
    L = int(input())
    Ml, Mk = map(int, input().split())
    Cammo = int(input())
    Z = [int(input()) for _ in range(L)]

    # 1.
    used_Cammo = 0
    time = 0
    for idx in range(L):
        z = Z[idx] - time * Mk
        if z > min(idx - time, Ml) * Mk:
            used_Cammo += 1
            if Cammo > used_Cammo:
                print("NO")
                return
        time += math.floor(z / Mk)
    print("Yes")


solution()
