# https://school.programmers.co.kr/learn/courses/15008/lessons/121685
def func(gen, num):
    if gen == 1: return 'Rr'    # 1세대는 Rr
    parent = func(gen - 1, (num - 1) // 4 + 1)

    if parent == 'RR' or parent == 'rr': return parent  # 부모가 RR , rr 이라면 자식과 같기 때문

    if num % 4 == 0:    # 예시에서 rr은 8, 12번째 고로 4로 나눴을때 나머지 0
        return 'rr'
    elif num % 4 == 1: # 예시에서 RR은 5, 9 고로 4로 나눴을때 나머지 1
        return 'RR'
    else:               # 그 외는 전부 Rr
        return 'Rr'


def solution(queries):
    answer = []

    for query in queries:
        answer.append(func(query[0], query[1]))
    return answer