# [PCCP 모의고사 #1] 1번 외톨이 알파벳
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683
# 23-07-28


def solution(input_string):
    answer = ""
    is_outsider = [False] * 26
    alphabets = [-1] * 26
    for i in range(len(input_string)):
        idx = ord(input_string[i]) - ord("a")
        if is_outsider[idx] or alphabets[idx] + 1 == i or alphabets[idx] == -1:
            alphabets[idx] = i
            continue
        is_outsider[idx] = True
    answer = "".join(
        [chr(ord("a") + idx) for idx in range(len(is_outsider)) if is_outsider[idx]]
    )
    return answer if answer else "N"
