"""
Q. [BOJ] 1167. 트리의 지름
lv. G2
link: https://www.acmicpc.net/problem/1167
"""


import sys
sys.stdin = open('input.txt', 'r')


import heapq


def solution():
    answer = [0]

    def dfs(cur, prev, prev_dist, cur_w):
        dists = [0]
        for adj, w in tree[cur]:
            if adj == prev:
                continue
            dists.append(dfs(adj, cur, prev_dist + cur_w, w))
        max_dist = sum(heapq.nlargest(2, dists + [prev_dist + cur_w]))
        answer[0] = max(answer[0], max_dist)
        return max(dists) + cur_w

    V = int(input())
    tree = [[] for _ in range(V + 1)]

    for _ in range(V):
        n, *adj_nodes, _ = map(int, input().split())
        for adj, w in zip(adj_nodes[::2], adj_nodes[1::2]):
            tree[n].append((adj, w))

    dfs(1, 0, 0, 0)

    return answer[0]


if __name__ == '__main__':
    res = solution()
    print(res)