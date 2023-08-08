"""
쓰라이딩 윈다우
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = sorted(list(map(int, sys_input().split())))

    begin, end = 0, n - 1
    answer = [nums[begin], nums[end]]
    closest = abs(nums[begin] + nums[end])

    while begin < end:
        total = nums[begin] + nums[end]

        if closest > abs(total):
            answer = [nums[begin], nums[end]]
            closest = abs(total)

        if total > 0:
            end -= 1
        else:
            begin += 1

    print(*answer)


solution()
