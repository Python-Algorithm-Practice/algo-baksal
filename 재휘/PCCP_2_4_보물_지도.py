"""
BFS
"""
from collections import deque


def is_not_valid_point(board, r, c):
    if r < 0 or len(board) <= r \
            or c < 0 or len(board[0]) <= c:
        return True

    return not board[r][c]


def is_not_reachable(min_dist_table, r, c):
    return min_dist_table[r][c] == -1


def get_min_dist_table(board, begin_r, begin_c):
    min_dist_table = [[-1] * len(board[0]) for _ in range(len(board))]
    min_dist_table[begin_r][begin_c] = 0

    visit = [[False] * len(board[0]) for _ in range(len(board))]
    visit[begin_r][begin_c] = True

    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    bfs_q = deque([[begin_r, begin_c]])

    while bfs_q:
        r, c = bfs_q.popleft()

        for direc in range(4):
            next_r = r + dr[direc]
            next_c = c + dc[direc]

            if is_not_valid_point(board, next_r, next_c) \
                    or visit[next_r][next_c]:
                continue

            min_dist_table[next_r][next_c] = min_dist_table[r][c] + 1

            visit[next_r][next_c] = True
            bfs_q.append([next_r, next_c])

    return min_dist_table


def solution(n, m, hole):
    # 지도 생성
    board = [[True] * n for _ in range(m)]
    for c, r in hole:
        board[r - 1][c - 1] = False

    # (1, 1), (n, m) 부터 각 지점까지 최단 거리 구하기
    from_begin = get_min_dist_table(board, 0, 0)
    from_end = get_min_dist_table(board, m - 1, n - 1)

    # 짬프했을 때 최단 거리 구하기
    dr, dc = [2, 0], [0, 2]  # 짬프는 두 칸
    answer = n * m  # 초기값 최대루

    for r in range(m):
        for c in range(n):
            if is_not_valid_point(board, r, c):
                continue

            for direc in range(2):
                next_r = r + dr[direc]
                next_c = c + dc[direc]

                if is_not_valid_point(board, next_r, next_c):
                    continue

                if is_not_reachable(from_begin, r, c) \
                        or is_not_reachable(from_end, next_r, next_c):
                    continue

                answer = min(
                    answer,
                    from_begin[r][c] + from_end[next_r][next_c] + 1
                )

    return answer if answer != n * m else -1


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
print(solution(3, 3, [[2, 1], [2, 2], [2, 3], [3, 1], [3, 2]]))
