"""
Q. 프로세스
link: https://school.programmers.co.kr/learn/courses/30/lessons/42587
key: 스택/큐
"""

from collections import deque, Counter


def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    search = sorted(priorities, reverse=True)

    while queue:
        item = queue.popleft()

        if search[answer] == item[1]:
            answer += 1
            if item[0] == location:
                break
        else:
            queue.append(item)

    return answer


def solution(priorities, location):
    answer = 0

    queue = deque(enumerate(priorities))
    counter = sorted([[i, cnt] for i, cnt in Counter(priorities).items()], reverse=True)
    counter_idx = 0
    while queue:
        loc, priority = queue.popleft()
        if priority == counter[counter_idx][0]:
            answer += 1
            counter[counter_idx][1] -= 1
            if counter[counter_idx][1] == 0:
                counter_idx += 1
            if loc == location:
                break
        queue.append((loc, priority))

    return answer



if __name__ == '__main__':
    in_data = [2, 1, 3, 2], 2
    res = solution(*in_data)
    print(res)  # 1

    in_data = [1, 1, 9, 1, 1, 1], 0
    res = solution(*in_data)
    print(res)  # 5
