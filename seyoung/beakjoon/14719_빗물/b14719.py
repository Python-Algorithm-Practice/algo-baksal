"""
Q. [BOJ] 14719. 빗물
lv. G5
link: https://www.acmicpc.net/problem/14719
"""


class Block:
    def __init__(self, height, pos):
        self.height = height
        self.pos = pos

    def __gt__(self, other):
        return self.height > other.height

    def __le__(self, other):
        return self.height <= other.height

    def __str__(self):
        return f"{self.height} {self.pos}"

    def __repr__(self):
        return str(self)


def solution(max_h: int, max_w: int, heights: list[int]) -> int:
    answer = 0

    stack = []
    for i, height in enumerate(heights):
        new_block = Block(height, i)

        while len(stack) >= 2 and stack[-1] <= new_block:
            prev_block = stack.pop()
            h = min(stack[-1].height, new_block.height) - prev_block.height
            w = new_block.pos - stack[-1].pos - 1
            answer += h * w

        if stack and height > stack[-1].height:
            stack.pop()
        stack.append(new_block)

    return answer


def main():
    h, w = map(int, input().split())
    heights = list(map(int, input().split()))
    res = solution(h, w, heights)
    print(res)


if __name__ == "__main__":
    main()

