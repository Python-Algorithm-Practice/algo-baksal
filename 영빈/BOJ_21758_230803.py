# 꿀 따기 gold 5
# https://www.acmicpc.net/problem/21758
# 23-08-03  누적합
import sys


def solution():
    # 0. input 받기
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    if N == 3:
        print(max(arr) * 2)
        return

    # 1. 순방향, 역방향 누적합 만들기
    prefix_sum = [arr[0]] * N
    postfix_sum = [arr[-1]] * N
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    for i in range(N - 1, 0, -1):
        postfix_sum[i - 1] = postfix_sum[i] + arr[i - 1]

    # 2. 꿀의 최댓값 구하기
    # 2-0. max(-arr[n]+S(arr[n+-1]))에 해당하는 배열 구하기
    postfix_max = [float("-inf")] * N
    for j in range(1, N - 1):
        postfix_max[j] = max(postfix_max[j - 1], -arr[j] + postfix_sum[j + 1])
    prefix_max = [float("-inf")] * N
    for j in range(N - 2, 0, -1):
        prefix_max[j] = max(prefix_max[j + 1], -arr[j] + prefix_sum[j - 1])

    max_honey = max(
        # i = 0: 오른쪽에서만 가능
        prefix_sum[N - 2] + prefix_max[1],
        # i = 1: 양방향과 오른쪽에서 가능
        arr[1] + (prefix_sum[N - 2] - prefix_sum[0]),
        prefix_sum[N - 2] - prefix_sum[0] * 2 + prefix_max[2],
        # i = N-2: 양방향과 왼쪽에서 가능
        (postfix_sum[1] - postfix_sum[N - 1]) + arr[N - 2],
        postfix_sum[1] - postfix_sum[N - 1] * 2 + postfix_max[N - 2],
        # i = N-1: 왼쪽에서만 가능
        postfix_sum[1] + postfix_max[N - 1],
    )
    for i in range(2, N - 2):
        # 2-1. 왼쪽
        max_honey = max(
            max_honey,
            postfix_sum[1] - postfix_sum[i + 1] * 2 + postfix_max[i],
        )
        # 2-2. 양방향
        max_honey = max(
            max_honey,
            (postfix_sum[1] - postfix_sum[i + 1])
            + (prefix_sum[N - 2] - prefix_sum[i - 1]),
        )
        # 2-3. 오른쪽
        max_honey = max(
            max_honey,
            prefix_sum[N - 2] - prefix_sum[i - 1] * 2 + prefix_max[i + 1],
        )
    print(max_honey)
    return


solution()
