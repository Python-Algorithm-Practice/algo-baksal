"""
Q. [BOJ] 14719. 빗물
lv. G5
link: https://www.acmicpc.net/problem/14719
"""


def solution(h: int, w: int, heights: list[int]) -> int:
    left_max_heights = [0] * w
    right_max_heights = [0] * w

    left_max_heights[0] = heights[0]
    right_max_heights[-1] = heights[-1]

    for i in range(1, w):
        left_max_heights[i] = max(left_max_heights[i - 1], heights[i])
        right_max_heights[-i - 1] = max(right_max_heights[-i], heights[-i - 1])

    answer = sum(min(left_max_heights[i], right_max_heights[i]) - heights[i] for i in range(w))
    return answer


def solution(h: int, w: int, heights: list[int]) -> int:
    airs = [0] * w
    left_min_air = h
    for i, height in enumerate(heights):
        left_min_air = min(left_min_air, h - height)
        airs[i] = left_min_air

    right_min_air = h
    for i in range(w - 1, -1, -1):
        right_min_air = min(right_min_air, h - heights[i])
        airs[i] = max(airs[i], right_min_air)

    return h * w - sum(heights) - sum(airs)


def main():
    h, w = map(int, input().split())
    heights = list(map(int, input().split()))
    res = solution(h, w, heights)
    print(res)


if __name__ == "__main__":
    main()

