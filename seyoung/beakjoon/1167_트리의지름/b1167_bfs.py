"""
Q. [BOJ] 1167. 트리의 지름
lv. G2
link: https://www.acmicpc.net/problem/1167
"""


import sys
sys.stdin = open('input.txt', 'r')


from collections import deque


def solution():
    def bfs(start):
        visited = [False for _ in range(V + 1)]
        queue = deque([(start, 0)])
        visited[start] = True

        max_idx, max_dist = start, 0

        while queue:
            cur, dist = queue.popleft()

            if dist > max_dist:
                max_dist = dist
                max_idx = cur

            for adj, d in tree[cur]:
                if visited[adj]:
                    continue
                visited[adj] = True
                queue.append((adj, dist + d))

        return max_idx, max_dist

    V = int(input())
    tree = [[] for _ in range(V + 1)]

    for _ in range(V):
        n, *adj_nodes, _ = map(int, input().split())
        for adj, w in zip(adj_nodes[::2], adj_nodes[1::2]):
            tree[n].append((adj, w))

    idx, dist = bfs(1)
    idx, dist = bfs(idx)
    return dist


if __name__ == '__main__':
    res = solution()
    print(res)