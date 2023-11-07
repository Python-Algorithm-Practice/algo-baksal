from collections import defaultdict


def solution(info, edges):
    tree = defaultdict(list)
    for v1, v2 in edges:
        tree[v1].append(v2)

    max_sheep = 0

    def dfs(cur, stack, sheep, wolf):
        nonlocal max_sheep

        if info[cur]:
            wolf += 1
        else:
            sheep += 1
            max_sheep = max(max_sheep, sheep)

        stack.extend(tree[cur])

        for i, n in enumerate(stack):
            if sheep - wolf > info[n]:
                dfs(n, stack[:i] + stack[i+1:], sheep, wolf)

    dfs(0, [], 0, 0)

    return max_sheep