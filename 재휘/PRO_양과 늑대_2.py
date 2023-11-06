"""
BFS + Permutation
"""
from collections import deque
from itertools import permutations


class Animal:
    def __init__(self, animal_id, animal_type):
        self.id = animal_id
        self.animal_type = animal_type
        self.child = []
        self.wolves = set()

    def add_child(self, child_animal):
        self.child.append(child_animal)

    def add_wolf(self, wolf):
        self.wolves.add(wolf)

    def update_wolves(self, wolves):
        self.wolves.update(wolves)

    def is_sheep(self):
        return self.animal_type == 0

    def is_wolf(self):
        return self.animal_type == 1


def get_tree(info, edges):
    animals = [Animal(animal_id, animal_type) for animal_id, animal_type in enumerate(info)]

    for parent, child in edges:
        animals[parent].add_child(animals[child])

    return animals


def set_wolves(root):
    bfs_q = deque([root])

    while bfs_q:
        front = bfs_q.popleft()

        if front.is_wolf():
            front.add_wolf(front.id)

        for child_animal in front.child:
            child_animal.update_wolves(front.wolves)
            bfs_q.append(child_animal)


def simulate(sheep_list, free_sheep_count):
    sheep_count = free_sheep_count
    wolves = set()

    for sheep in sheep_list:
        if sheep_count <= len(wolves.union(sheep.wolves)):
            break
        sheep_count += 1
        wolves.update(sheep.wolves)

    return sheep_count


def solution(info, edges):
    animals = get_tree(info, edges)

    set_wolves(animals[0])

    sheep_list = [animal for animal in animals if animal.is_sheep()]

    filtered_sheep_list = [sheep for sheep in sheep_list if len(sheep.wolves) != 0]

    answer = 0
    free_sheep_count = len(sheep_list) - len(filtered_sheep_list)

    for perm in permutations(filtered_sheep_list, len(filtered_sheep_list)):
        answer = max(answer, simulate(perm, free_sheep_count))

    return answer


solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])
solution([0,1,0,1,1,0,1,0,0,1,0]	, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])
