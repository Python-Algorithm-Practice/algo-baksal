import sys
input = sys.stdin.readline

tc = int(input())


def bf():
    for i in range(n):
        for j in range(len(edges)):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False


for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    dist = [int(1e9)] * (n + 1)

    for i in range(m+w):

        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))

    if bf():
        print('YES')
    else:
        print('NO')
