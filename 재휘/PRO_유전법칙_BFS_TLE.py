"""
BFS
"""
from collections import deque


def bfs(query):
    child_of = {
        'Rr': ['RR', 'Rr', 'Rr', 'rr'],
        'RR': ['RR' for _ in range(4)],
        'rr': ['rr' for _ in range(4)]
    }

    bfs_q = deque(['Rr'])
    for _ in range(1, query[0]):
        q_size = len(bfs_q)
        for _ in range(q_size):
            front = bfs_q.popleft()
            bfs_q.extend(child_of[front])

    return bfs_q[query[1] - 1]


def solution(queries):
    return [bfs(query) for query in queries]


print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
