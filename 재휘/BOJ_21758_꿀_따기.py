"""
누적합
"""
import sys


def solution():
    sys_input = sys.stdin.readline

    n = int(sys_input())
    nums = [None] + list(map(int, sys_input().split()))  # 인덱스 맞추기용 None

    # 누적합 배열 생성
    p_sum = [0] + [nums[i] for i in range(1, len(nums))]
    r_sum = [None] + [nums[i] for i in range(1, len(nums))] + [0]

    for i in range(1, len(p_sum)):
        p_sum[i] += p_sum[i - 1]

    for i in range(len(r_sum) - 2, 0, -1):
        r_sum[i] += r_sum[i + 1]

    max_honey = 0

    # 벌집이 맨 왼쪽, 벌 한 마리가 맨 오른쪽에 있을 때 나머지 한 마리를 배치하며 최댓값 탐색
    # ex) _ h . . . . . . b
    for i in range(2, len(nums) - 1):
        max_honey = max(max_honey, p_sum[-2] + p_sum[i - 1] - nums[i])

    # 벌집이 맨 오른쪽, 벌 한 마리가 맨 왼쪽에 있을 때 나머지 한 마리를 배치하며 최댓값 탐색
    # ex) _ b . . . . . . h _
    for i in range(2, len(nums) - 1):
        max_honey = max(max_honey, r_sum[2] + r_sum[i + 1] - nums[i])

    # 벌 두 마리가 맨 양쪽에 있을 때 벌집을 사이의 꽃들 중 최댓값에 위치시키고 계산하기
    # ex) b . . . . . . b
    max_honey = max(max_honey, sum(nums[2:-1]) + max(nums[2:-1]))

    print(max_honey)


solution()
