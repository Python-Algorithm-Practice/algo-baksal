# 괄호 제거 gold 4
# https://www.acmicpc.net/problem/2800
# 24-07-24  python 3 	31120 KB	48 ms

from itertools import combinations

def solution():
    equation = list(input())
    open_brackets = []
    bracket_pairs = []
    generated_equations = set()
    for i in range(len(equation)):
        if equation[i] == "(":
            open_brackets.append(i)
        elif equation[i] == ")":
            bracket_pairs.append((open_brackets.pop(), i))
    
    for r in range(1, len(bracket_pairs) + 1):
        for combi in combinations(bracket_pairs, r):
            to_erase = set()
            for op, cl in combi:
                to_erase.add(op)
                to_erase.add(cl)
            eq = []
            for i in range(len(equation)):
                if i in to_erase:
                    continue
                eq.append(equation[i])
            generated_equations.add("".join(eq))

    print('\n'.join(sorted(generated_equations)))
    return

solution()