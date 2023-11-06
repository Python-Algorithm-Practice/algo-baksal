from collections import deque
from itertools import permutations


class Node:
    def __init__(self, node_id, data):
        self.node_id = node_id
        self.data = data
        self.wolf_set = set()
        self.childs = []


def get_wolf_set(node, wolf_set):
    if node.data == 0:
        node.wolf_set.update(wolf_set)
    else:
        wolf_set.add(node.node_id)

    for child in node.childs:
        get_wolf_set(child, wolf_set)

    if node.data == 1:
        wolf_set.remove(node.node_id)


def make_tree(info, edges):
    nodes = [Node(node_id, data) for node_id, data in enumerate(info)]

    for edge in edges:
        nodes[edge[0]].childs.append(nodes[edge[1]])
    get_wolf_set(nodes[0], set())

    return nodes


def bfs_for_getting_sheep(root):
    sheep_set_list = []

    bfsq = deque()
    bfsq.append(root)
    while len(bfsq) > 0:
        qsize = len(bfsq)
        for idx in range(qsize):
            front = bfsq[0]
            bfsq.popleft()

            if front.data == 0:
                sheep_set_list.append(front.wolf_set)

            for child in front.childs:
                bfsq.append(child)

    return sheep_set_list


def solution(info, edges):
    nodes = make_tree(info, edges)
    root = nodes[0]

    sheep_list = bfs_for_getting_sheep(root)
    free_sheep = sheep_list.count(set())
    sheep_list = [data_set for data_set in sheep_list if data_set != set()]

    answer = 0

    for perm in permutations(sheep_list, len(sheep_list)):
        sheep_count = free_sheep
        wolf_set = set()
        for new_wolf_set in perm:
            if sheep_count <= len(new_wolf_set.union(wolf_set)):
                break
            sheep_count += 1
            wolf_set.update(new_wolf_set)

        if answer < sheep_count:
            answer = sheep_count

    return answer
