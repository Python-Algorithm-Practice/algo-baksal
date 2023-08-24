"""
Q. [BOJ] 2470. 두 용액
lv. G5
link: https://www.acmicpc.net/problem/2470
"""
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
print('expected: -99 98')


def solution():
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    answer = None

    min_sum = 2_000_000_000
    left, right = 0, N - 1
    while left < right:
        cur_sum = lst[left] + lst[right]
        abs_cur_sum = abs(cur_sum)
        if abs_cur_sum < min_sum:
            min_sum = abs_cur_sum
            answer = lst[left], lst[right]
        if cur_sum < 0:
            left += 1
        else:
            right -= 1
    print(f'{answer[0]} {answer[1]}')


if __name__ == '__main__':
    solution()
