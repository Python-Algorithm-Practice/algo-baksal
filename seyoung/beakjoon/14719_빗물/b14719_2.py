"""
Q. [BOJ] 14719. 빗물
lv. G5
link: https://www.acmicpc.net/problem/14719
"""


def solution(max_h: int, max_w: int, heights: list[int]) -> int:
    answer = 0

    stack = []
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] <= height:
            bottom_idx = stack.pop()
            if not stack:
                break
            w = i - stack[-1] - 1
            h = min(height, heights[stack[-1]]) - heights[bottom_idx]
            answer += w * h

        stack.append(i)

    return answer


def main():
    h, w = map(int, input().split())
    heights = list(map(int, input().split()))
    res = solution(h, w, heights)
    print(res)


if __name__ == "__main__":
    main()

