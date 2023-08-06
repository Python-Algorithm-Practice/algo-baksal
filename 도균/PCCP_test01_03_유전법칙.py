## pccp_test01_03_유전법칙
## https://school.programmers.co.kr/learn/courses/15008/lessons/121685

def Finder(gen, num):
    ## 1세대 : Rr
    if gen == 1:
        return "Rr"

    ## 전체 4 등분
    cutter = 4 ** (gen - 2)

    ## 첫 번째 쿼터 : RR
    if num <= cutter * 1:
        return "RR"

    ## 2nd 쿼터 : 앞 세대로 보내기
    elif cutter * 1 < num and num <= cutter * 2:
        if gen == 2:
            return "Rr"
        return Finder(gen - 1, num - cutter * 1)

    ## 3nd 쿼터 : 앞 세대로 보내기
    elif cutter * 2 < num and num <= cutter * 3:
        if gen == 2:
            return "Rr"
        return Finder(gen - 1, num - cutter * 2)

    ## 4th 쿼터 : rr
    elif cutter * 3 + 1 <= num:
        return "rr"


def solution(queries):
    answer = []
    for gen, num in queries:
        answer += [Finder(gen, num)]
    return answer