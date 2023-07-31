"""
비트마스킹
"""


def find_max(ability, visit, col, memo):
    if col == len(ability[0]):
        return 0
    if memo[visit][col] != -1:
        return memo[visit][col]

    max_value = 0

    for i in range(len(ability)):
        if (visit & (2 ** i)) == 0:
            max_value = max(max_value, ability[i][col] + find_max(ability, visit | (2 ** i), col + 1, memo))

    memo[visit][col] = max_value
    return memo[visit][col]


def solution(ability):
    memo = [[-1] * len(ability[0]) for _ in range(1 << len(ability))]
    return find_max(ability, 0, 0, memo)


print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))
