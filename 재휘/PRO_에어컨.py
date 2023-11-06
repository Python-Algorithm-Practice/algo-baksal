"""

"""
import sys


def solution(temperature, t1, t2, a, b, onboard):
    sys.setrecursionlimit(1_000_000)

    def find_min(cur_temperature, idx, memo):
        # 끝까지 도달하면 종료
        if idx == len(onboard):
            return 0

        # 범위를 벗어날 경우 (임의로 정한 범위)
        if cur_temperature < -100 or 100 < cur_temperature:
            return -1

        # 이미 탐색한 적이 있는 경우
        if memo[cur_temperature][idx] != -1:
            return memo[cur_temperature][idx]

        # 손님 탔는데 온도 조절이 개판된 경우
        if onboard[idx] and (cur_temperature < t1 or t2 < cur_temperature):
            return -1

        min_value = int(1e10)
        amounts = [1, 0, -1]  # 온도 증가, 유지, 감소
        powers = [
            a if temperature <= cur_temperature else 0,  # 실외 온도 이상이면 a 전력, 아니라면 실외 온도와 같아지는 방향이므로 0
            b if temperature != cur_temperature else 0,  # 실외 온도와 다르다면 전력 b, 아니라면 실외 온도와 같으므로 0
            a if cur_temperature <= temperature else 0  # 실외 온도 이하면 b 전력, 그 외 0
        ]

        # 온도 증가, 유지, 감소 순서로 재귀 호출
        for amount, power in zip(amounts, powers):
            value = find_min(cur_temperature + amount, idx + 1, memo)
            if value == -1:  # 불가능할 경우 패쓰
                continue

            min_value = min(min_value, value + power)

        memo[cur_temperature][idx] = min_value

        return min_value

    # 문제에서 주어진 temperature 조건은 [-10, 40]이지만 온도를 쭉 올렸다가 내릴 수 있으므로 넉넉하게 잡음
    dp = {temp: [-1] * 1000 for temp in range(-100, 101)}

    return find_min(temperature, 0, dp)


print(solution(28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]))
print(solution(-10, -5, 5, 5, 1, [0, 0, 0, 0, 0, 1, 0]))
print(solution(11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))
print(solution(11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))
