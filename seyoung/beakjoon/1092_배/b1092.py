"""
Q. [BOJ] 1092. 배
lv. G5
link: https://www.acmicpc.net/problem/1092
"""


import sys
sys.stdin = open('input.txt', 'r')


def solution():
    def search(target: int):
        left, right = 0, len(weights) - 1
        while left <= right:
            mid = (left + right) // 2

            if weights[mid] == target:
                right = mid
                break
            elif weights[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    N = int(input())
    limits = list(map(int, input().split()))
    M = int(input())
    weights = list(map(int, input().split()))

    answer = 0

    limits.sort(reverse=True)
    weights.sort()

    while weights and weights[-1] <= limits[0]:
        answer += 1
        for crane in limits:
            w_idx = search(crane)

            if w_idx >= 0:
                weights.pop(w_idx)
            if not weights:
                return answer

    return answer if not weights else -1


if __name__ == '__main__':
    res = solution()
    print(res)
