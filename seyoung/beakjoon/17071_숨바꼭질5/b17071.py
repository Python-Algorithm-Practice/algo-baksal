"""
Q. [BOJ] 17071. 숨바꼭질 5
lv. P5
---
어떤 점 x에 t초에 도달할 수 있다면, t+2, t+4, t+6, ... 에도 x에 도달할 수 있습니다.
좌우로 한 번 왔다갔다하면 다시 제자리로 돌아오기 때문입니다.
"""


def sister_generator(k):
    time = 0
    while k <= 500_000:
        yield k
        time += 1
        k += time


def subin_generator(n):
    if n > 1:
        yield n - 1
    if n + 1 <= 500_000:
        yield n + 1
    if n * 2 <= 500_000:
        yield n * 2


def solution(n: int, k: int) -> int:
    # n: 수빈, k: 동생 -> 찾을 수 있는 가장 빠른 시간 answer 초
    visited = [[False] * 500_001 for _ in range(2)]
    visited[0][n] = True
    queue = [n]
    for time, k in enumerate(sister_generator(k)):
        idx = time % 2
        if visited[idx][k]:
            return time

        next_idx = (time + 1) % 2
        next_queue = []
        for pos in queue:
            for new_pos in subin_generator(pos):
                if visited[next_idx][new_pos]:
                    continue
                visited[next_idx][new_pos] = True
                next_queue.append(new_pos)
        queue = next_queue

    return -1


def main():
    n, k = map(int, input().split())
    res = solution(n, k)
    print(res)


if __name__ == "__main__":
    main()

    # print(solution(5, 17))


