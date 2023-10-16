
""" 골드 3. 드래곤 커브 """

import sys
from collections import deque

input = sys.stdin.readline

def solution():

    N = int(input())        # 드래곤 커브의 개수

    dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]    # 드래곤 커브의 시작위치를 위한 방향 배열
    answer = []                                 # 드래곤 커브의 점들 위치를 저장

    for _ in range(N):

        x, y, d, g = map(int, input().split())    # 시작점 x, y / 시작방향 d / 세대 g
        q = deque()

        # 1. 드래곤 커브의 시작 위치 
        q.append((x, y))
        q.append((x + dir[d][0], y + dir[d][1]))

        # 2. 세대만큼 회전
        for _ in range(g):

            endx, endy = q[-1]      # 기준이 되는 끝점

            # 위치 계산
            for _ in range(len(q)-1):
                startx, starty = q.popleft()
                q.append((startx, starty))
                q.append((endx + endy - starty, endy - endx + startx))
        
        # 3. 최종 드래곤 코드에 추가
        answer += q

    answer = set(answer)

    # 4. 정사각형 개수 구하기
    sx, sy = min(answer, key=lambda x : x[0])[0], min(answer, key=lambda x : x[1])[1]
    ex, ey = max(answer, key=lambda x : x[0])[0], max(answer, key=lambda x : x[1])[1]
    
    count = 0

    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            if (x, y) in answer and (x+1, y) in answer and (x, y+1) in answer and (x+1, y+1) in answer:
                count += 1
    
    return count

print(solution())