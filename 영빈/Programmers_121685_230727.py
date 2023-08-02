# [PCCP 모의고사 #1] 3번 유전법칙
# https://school.programmers.co.kr/learn/courses/15008/lessons/121685
# 23-07-27  recursion

from math import pow


def solution(queries):
    answer = []

    def recursive(gen, order):
        if gen == 1:
            return "Rr"
        elif gen == 2:
            if order == 1:
                return "RR"
            elif order == 2 or order == 3:
                return "Rr"
            elif order == 4:
                return "rr"
        elif order > 0 and order <= pow(4, gen - 2):
            return "RR"
        elif order > pow(4, gen - 2) and order <= 2 * pow(4, gen - 2):
            return recursive(gen - 1, order - pow(4, gen - 2))
        elif order > 2 * pow(4, gen - 2) and order <= 3 * pow(4, gen - 2):
            return recursive(gen - 1, order - 2 * pow(4, gen - 2))
        elif order > 3 * pow(4, gen - 2) and order <= pow(4, gen - 1):
            return "rr"

    for gen, order in queries:
        answer.append(recursive(gen, order))

    return answer
