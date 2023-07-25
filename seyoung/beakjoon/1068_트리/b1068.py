"""
Q. [BOJ] 1069. 트리
lv. G5
key. Tree, DFS
"""
from collections import defaultdict


def solution():
    N = int(input())
    parents = list(map(int, input().split()))
    deleted_node = int(input())

    parents[deleted_node] = -2  # 노드 삭제

    root = -1
    tree = defaultdict(list)
    for i, p in enumerate(parents):
        # 부모 노드에 자식 이어주기
        tree[p].append(i)
        if p == -1:
            root = i    # 루트 노드

    if root < 0:
        print(0)
        return

    # 루트 노드부터 순회하며 리프 노드 찾기
    answer = 0
    stack = [root]
    while stack:
        cur = stack.pop()

        if not tree[cur]:
            answer += 1
            continue

        for child in tree[cur]:
            stack.append(child)

    print(answer)


if __name__ == '__main__':
    solution()


