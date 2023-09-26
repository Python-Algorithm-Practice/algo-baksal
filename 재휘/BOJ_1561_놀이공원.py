"""
이분 탐색
"""
import sys


# 이분 탐색
# 조건 : 시간
# 내용 : 특정 시간일 경우 모든 아이들을 태울 수 있는지. 없다면 시간을 늘리고, 있다면 시간을 낮춰서 최적값 찾고!
def find_last_minute(n, nums):
    min_minutes = 0
    max_minutes = 2_000_000_000 * 30
    last_minute = max_minutes

    while min_minutes < max_minutes:
        mid = (min_minutes + max_minutes) >> 1

        # 태울 수 있는 아이들의 수
        covered = len(nums)
        for num in nums:
            covered += mid // num

        # 태울 수 없다면 시간 늘리기
        if covered < n:
            min_minutes = mid + 1
        # 태울 수 없다면 시간을 줄여 최적값 찾기 & 최적값 갱신
        else:
            max_minutes = mid
            last_minute = mid

    # min, max minutes가 같을 땐 고려 안 했으므로 마지막으로 한 번 더
    covered = len(nums)
    for num in nums:
        covered += max_minutes // num

    if covered >= n:
        last_minute = max_minutes

    return last_minute


def solution():
    sys_input = sys.stdin.readline

    n, m = map(int, sys_input().split())
    nums = list(map(int, sys_input().split()))

    last_minute = find_last_minute(n, nums)

    # 직전까지 탄 애들은 모두 빼기
    prev_ended = m
    for num in nums:
        prev_ended += (last_minute - 1) // num

    # 남은 애들 중에서 마지막 아이를, last_minutes로 나누어 떨어지는 기구 중 몇 번째 기구에 태워야 하는지 구하기
    answer = [idx + 1 for idx, num in enumerate(nums) if last_minute % num == 0][n - prev_ended - 1]
    print(answer)


solution()
