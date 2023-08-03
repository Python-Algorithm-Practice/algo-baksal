
""" [프로그래머스 PCCP 모의고사 #1] 외톨이 알파벳 """

def solution(input_string):
    answer = ''

    for i, s in enumerate(input_string):

        if s in answer:
            continue

        if s in input_string[i+2:] and input_string[i+1] != s:
            answer += s

    if not answer:
        return "N"
    
    answer = "".join(sorted(answer))
    return answer


print(solution("edeaaabbccd"))      # "de"
print(solution("eeddee"))           # "e"
print(solution("string"))           # "N"
print(solution("zbzbz"))            # "bz"