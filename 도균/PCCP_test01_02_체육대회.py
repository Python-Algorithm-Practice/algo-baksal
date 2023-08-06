## PCCP_test01_02_체육대회
## https://school.programmers.co.kr/learn/courses/15008/lessons/121684

from itertools import permutations

def solution(ability):
    answer = []
    len_students = len(ability)
    len_subjects = len(ability[0])

    permus = list(permutations(range(len_students), len_subjects))

    for permu in permus:
        temp = 0
        for i in range(len_subjects):
            temp += ability[permu[i]][i]
        answer.append(temp)

    return max(answer)