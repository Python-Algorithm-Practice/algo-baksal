
""" [프로그래머스] Level 2. 다리를 지나는 트럭 """

from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 1
    queue = deque()

    total = truck_weights.pop(0)
    queue.append(total)

    while total > 0:

        answer += 1

        if len(queue) == bridge_length:
            total -= queue.popleft()

        if truck_weights and total + truck_weights[0] <= weight:
            total += truck_weights[0]
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)

    return answer


# 다리에 올라갈 수 있는 최대 트럭 수, 다리가 견딜 수 있는 무게, 트럭별 무게
print(solution(2, 10, [7,4,5,6]))                               # 8
print(solution(100, 100, [10]))                                 # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))      # 110

print(solution(4, 2, [1, 1, 1, 1]))                             # 10