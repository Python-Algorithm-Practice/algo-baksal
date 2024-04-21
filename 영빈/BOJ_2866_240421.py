# 문자열 잘라내기   gold 5
# https://www.acmicpc.net/problem/2866
# 24-04-21  python 3    51608 KB	460 ms

def solution():
    R, C = map(int, input().split())
    table = [list(input()) for _ in range(R)]
    strings = [[table[r][c] for r in range(R)] for c in range(C)]

    def compare(start: int, end:int):
        substrings = set()
        for i in range(C):
            substrings.add(str(strings[i][start:]))
            if len(substrings) <= i:
                return True
        return False

    left = 0
    right = R-1
    while left < right:
        mid = (left+right)//2
        if compare(mid+1, right):
            right = mid
            continue
        left = mid+1
    answer = (left+right)//2
    return print(answer)

solution()