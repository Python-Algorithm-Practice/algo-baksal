"""
우선순위 큐
"""
import sys
from heapq import heappush, heappop


def value(min_heap, key):
    if key == 'VALUE':
        return min_heap[0][0]
    if key == 'INDEX':
        return min_heap[0][1]


def mod_query(min_heap, i, v, latest):
    heappush(min_heap, (v, i))
    latest[i] = v


def print_query(min_heap, latest):
    while is_old_value(min_heap, latest):
        heappop(min_heap)
    print(value(min_heap, 'INDEX'))


def is_old_value(min_heap, latest):
    return value(min_heap, 'VALUE') != latest[value(min_heap, 'INDEX')]


def solution():
    sys_input = sys.stdin.readline

    # 입력
    n = int(sys_input())
    nums = [None] + list(map(int, sys_input().split()))

    m = int(sys_input())

    # 최소 힙, 최신 값 저장용 딕셔너리 생성
    min_heap = []
    latest = dict()
    for idx in range(1, len(nums)):
        heappush(min_heap, (nums[idx], idx))
        latest[idx] = nums[idx]

    # 쿼리 처리
    for _ in range(m):
        query = list(map(int, sys_input().split()))
        if query[0] == 1:
            mod_query(min_heap, query[1], query[2], latest)
        else:
            print_query(min_heap, latest)


solution()
