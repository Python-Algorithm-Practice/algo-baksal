"""
사?진 트리

이진 트리처럼 정점을 배열로 나타냈을 때 아래의 특성을 가짐
    i번째 정점의 자식들 : (4i - 2), (4i - 1), (4i), (4i + 1)
    i번째 정점의 부모 : (i + 2) // 4
    ex)
                    1
        2       3       4       5
    6 7 8 9  10 11...
"""


def find_index(gen, p):
    index = 0

    for i in range(0, gen - 1):
        index += 4 ** i

    return index + p


def reversed_path(index):
    rev_path = []

    while index:
        rev_path.append(index)
        index = (index + 2) >> 2

    return rev_path


def find_type(rev_path):
    prev_gen = rev_path.pop()
    while rev_path:
        cur_gen = rev_path.pop()
        if 4 * prev_gen - 2 == cur_gen:
            return 'RR'
        elif 4 * prev_gen + 1 == cur_gen:
            return 'rr'
        prev_gen = cur_gen

    return 'Rr'


def solution(queries):
    answer = [find_type(reversed_path(find_index(gen, p))) for gen, p in queries]
    return answer


print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
