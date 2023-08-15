
""" [백준] 골드 5. 꿀 따기 """

import sys

def solution():

    N = int(sys.stdin.readline())                        # 장소 수
    H = list(map(int, sys.stdin.readline().split()))     # 각 장소에서 딸 수 있는 꿀의 양
    S = [H[i] for i in range(N)]                         # 누적합

    for i in range(1,N):
        S[i] += S[i-1]

    answer = 0
    count = 0

    for idx in range(N):

        if idx == 0:
            for i in range(1, N-1):
                count = max(count, S[i-1] + (S[N-1] - H[N-1] - H[i]))
        elif idx == N-1:
            for i in range(1, N-1):
                count = max(count, (S[N-1] - H[0] - H[i]) + (S[N-1] - S[i]))
        else:
            count = (S[idx] - H[0]) + (S[N-2] - S[idx-1])

        answer = max(answer, count)

    print(answer)

if __name__ == '__main__':
    solution()