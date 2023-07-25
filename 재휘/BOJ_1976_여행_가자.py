"""
쁠로이드 와쌸
"""
import sys


def check(nodes, plan):
    for i in range(1, len(plan)):
        begin = plan[i - 1]
        end = plan[i]
        if begin == end:
            continue
        if not nodes[begin][end]:
            return 'NO'

    return 'YES'


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    _ = int(sys_input())
    nodes = [list(map(int, sys_input().split())) for _ in range(n)]
    plan = list(map(lambda x: int(x) - 1, sys_input().split()))

    for via in range(n):
        for begin in range(n):
            for end in range(n):
                nodes[begin][end] |= nodes[begin][via] & nodes[via][end]

    print(check(nodes, plan))


solution()
