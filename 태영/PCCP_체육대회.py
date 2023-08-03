# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

from itertools import permutations

def solution(ability):
    answer = 0
    num = len(ability[0])   #과목개수
    d = list(permutations(ability, num))    #과목개수만큼 뽑는 순열 생성
    # print(d)
    for i in range(len(d)):
        result = 0
        for j in range(num):    #순열을 돌며 더하기
            result += d[i][j][j]
        answer = max(answer, result)
    return answer