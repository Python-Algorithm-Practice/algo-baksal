# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(p, l):
    answer = []
    a = []
    for i, j in enumerate(p):
        a.append([i, j])

    while a:
        pr = a.pop(0)
        # 우선순위가 더 높은 프로세스가 있는지 확인
        if any(pr[1] < i[1] for i in a):
            a.append(pr)
        else:
            answer.append(pr)

    for i in answer:
        if i[0] == l:
            return answer.index(i) + 1