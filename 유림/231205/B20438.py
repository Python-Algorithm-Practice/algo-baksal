
""" [백준] 실버 2. 출석체크"""

import sys

def solution():

    input = sys.stdin.readline
    N, K, Q, M = map(int, input().split())          # 학생 수 N, 졸고 있는 학생 수 K, 출석코드 보낼 학생 수 Q, 주어질 구간의 수 M
    k_student = list(map(int, input().split()))     # 졸고 있는 학생의 입장 번호
    q_student = list(map(int, input().split()))     # 출석 코드를 받을 학생의 입장 번호

    N += 3
    student = [0] * N

    for k in k_student:
        student[k] = -1

    for q in q_student:
        if student[q] == 0:
            idx = q
            while idx < N:
                if student[idx] == 0:
                    student[idx] = 1
                idx += q

    answer = [0] * N
    answer[3] = 0 if student[3] == 1 else 1

    for idx in range(4, N):
        answer[idx] = answer[idx-1] + (0 if student[idx] == 1 else 1)

    for _ in range(M):
        S, E = map(int, input().split())                # 구간의 범위 S, E
        print(answer[E] - answer[S-1])

solution()