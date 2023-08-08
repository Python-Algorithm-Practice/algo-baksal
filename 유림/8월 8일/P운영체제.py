
""" [프로그래머스 PCCP 모의고사 #1] 운영체제 """

import heapq

def solution(program):

    answer = [0] * 11
    heap = []                            # 우선순위 큐

    program.sort(key=lambda x: (x[1], x[0]))    # 호출된 시각과 우선순위를 기준으로 정렬

    time = 0

    while program or heap:
        
        while program and program[0][1] <= time:
            heapq.heappush(heap, program.pop(0))

        if program and not heap:
            time = program[0][1]
            heapq.heappush(heap, program.pop(0))

        temp = heapq.heappop(heap)

        answer[temp[0]] += (time - temp[1])
        time += temp[2]

    answer[0] = time
    return answer


# [우선순위, 호출된 시각, 실행 시간]
print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))     # [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))       # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]

print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 20, 5]]))      # [25, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0]