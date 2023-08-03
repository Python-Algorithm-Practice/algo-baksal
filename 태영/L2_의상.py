# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dict = {}
    dict2 = {}
    for i in range(len(clothes)):
        dict[clothes[i][0]] = clothes[i][1]

    for j in dict.values():
        dict2[j] = dict2.get(j, 0) + 1  #종류별 의상 갯수 카운트


    for i in dict2.values():
        answer *=  (i+1)        #경우의수 구하기 e.g. 모자2개, 안경1개 일때 = (모자2+안썻을때1)(안경1+안썻을때1)
    return answer-1             #-1(아무것도 안입은경우의수)