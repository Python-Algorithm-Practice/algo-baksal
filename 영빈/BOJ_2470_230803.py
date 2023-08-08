# 두 용액 gold 5
# https://www.acmicpc.net/problem/2470
# 23-08-03  two pointer 42172 KB	124 ms


def solution():
    N = int(input())
    solutions = list(map(int, input().split()))
    solutions.sort()
    leftPtr = 0
    rightPtr = N - 1
    minDiff = 2000000000
    minPair = [leftPtr, rightPtr]
    while leftPtr < rightPtr:
        neutral = solutions[leftPtr] + solutions[rightPtr]
        minDiff = min(minDiff, abs(neutral))
        if minDiff == abs(neutral):
            minPair = [leftPtr, rightPtr]
        if neutral > 0:
            rightPtr -= 1
        elif neutral < 0:
            leftPtr += 1
        else:
            print(solutions[leftPtr], solutions[rightPtr])
            return
    print(solutions[minPair[0]], solutions[minPair[1]])
    return


solution()
