# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 22-05-08


def solution(priorities, location):
    answer = 0
    target = priorities[location]
    pointer = -1
    prior = max(priorities)
    while prior >= target:
        for i in priorities:
            if pointer == len(priorities) - 1:
                pointer = 0
            else:
                pointer += 1
            if i == prior:
                priorities[pointer] = -1
                answer += 1
                if pointer == location:
                    return answer
            prior = max(priorities)
