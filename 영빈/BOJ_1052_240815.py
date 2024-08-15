# 물병  gold 5
# https://www.acmicpc.net/problem/1052
# 24-08-15  Python 3    31252 KB	40 ms
#           PyPy 3      108080 KB	88 ms


def solution():
    answer = -1
    N, K = map(int, input().split())
    arr = list(map(int, bin(N)[2:]))
    if sum(arr) <= K:
        return print(0)
    target = 0
    bottle_cnt = 0
    for i in range(len(arr)):
        if arr[i]:
            bottle_cnt += 1
            target += 1 << (len(arr) - 1 - i)
            if bottle_cnt == K:
                target += 1 << (len(arr) - 1 - i)
                break
    answer = target - N
    return print(answer)

solution()