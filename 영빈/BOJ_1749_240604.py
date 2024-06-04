# 점수따먹기    gold 4
# https://www.acmicpc.net/problem/1749
# 24-06-04


def solution():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    prefix_sum = [[0]*M for _ in range(N)]

    # 0. 누적합 배열 만들기
    for c in range(M):
        prefix_sum[0][c] = arr[0][c]
    for r in range(N):
        prefix_sum[r][0] = arr[r][0]
    for r in range(1, N):
        for c in range(1, M):
            prefix_sum[r][c] = prefix_sum[r][c-1] + prefix_sum[r-1][c] - prefix_sum[r-1][c-1] + arr[r][c]

    # 1. 가장 큰 정사각형 구하기 (feat. 프로그래머스): dp
        # (x) dp[r][c]: 우하단 좌표가 (r, c)인 사각형 중 넓이가 최대인 사각형의 좌상단 좌표 (i, j)
        #           초기 값 = (r, c)
        #           갱신 값 = { dp[r-1][c]와 dp[r][c-1]의 좌표 값
        # (x) 가장 큰 정사각형들을 구해서 그 조합을..... 정사각형이 겹치면?ㅋㅋ 조짐~
    
    

    
    return

solution()