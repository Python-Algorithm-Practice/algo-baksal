
""" [백준] 골드 5. 배 """

import sys

input = sys.stdin.readline

def solution():

    N = int(input())                                    # 크레인의 개수
    crane_weight = list(map(int, input().split()))      # 각 크레인의 무게 제한
    M = int(input())                                    # 박스의 수
    box_weight = list(map(int, input().split()))        # 각 박스의 무게

    # 만약 모든 박스를 배로 옮길 수 없으면 
    if max(crane_weight) < max(box_weight):
        return -1
    
    # 박스를 배로 옮길 수 있으면
    crane_weight.sort(reverse=True)         # 내림차순  
    box_weight.sort()                       # 오름차순

    answer = 0
    
    # 가장 무거운 box부터 먼저 배로 옮기자
    while box_weight:
        
        # 제일 큰 crane부터 box 탐색
        for crane in crane_weight:                  

            # 가장 무거운 box부터 crane이 옮길 수 있는 box 탐색          
            idx = len(box_weight)-1              

            while box_weight and idx >= 0:          
                if box_weight[idx] <= crane:
                    box_weight.pop(idx)         # 옮긴 box는 삭제
                    break
                idx -= 1

        answer += 1     # 모든 크레인이 박스를 탐색했으니 하루 끝!

    return answer

print(solution())

    