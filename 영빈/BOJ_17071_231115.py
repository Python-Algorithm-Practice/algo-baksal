# 숨바꼭질 5 platinum 5
# https://www.acmicpc.net/problem/17071
# 23-11-15

from collections import deque


def solution():
    LEFT_BOUND = 0
    RIGHT_BOUND = 500001
    UNAVAILABLE = -1
    n, k = map(int, input().split())
    que = deque()
    visited = [
        0
    ] * RIGHT_BOUND  # 0: not visited, 1: 짝수초에 방문 가능, 2: 홀수초에 방문 가능, 3: 언제나 방문 가능
    cur_time = 0
    visited[n] = cur_time % 2 + 1
    que.append(n)
    if n == k:
        print(cur_time)
        return
    k += 1
    pos_cnt = len(que)

    def check_condition(position: int, time: int):
        meet = False
        if position < LEFT_BOUND or position >= RIGHT_BOUND:
            return meet
        if not visited[position] & (time % 2 + 1):
            visited[position] += time % 2 + 1
            que.append(position)
        return meet

    while que:
        cur_pos = que.popleft()
        pos_cnt -= 1
        next_positions = [cur_pos - 1, cur_pos + 1, cur_pos << 1]
        for next_pos in next_positions:
            if check_condition(next_pos, cur_time + 1):
                return
        if pos_cnt == 0:
            if k >= RIGHT_BOUND:
                print(UNAVAILABLE)
                return
            elif visited[k] & ((cur_time + 1) % 2 + 1):
                print(cur_time + 1)
                return
            cur_time += 1
            k += cur_time + 1
            pos_cnt = len(que)
    print(UNAVAILABLE)


solution()
