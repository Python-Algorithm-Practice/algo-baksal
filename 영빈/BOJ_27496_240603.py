# 발머의 피크 이론    silver 3
# https://www.acmicpc.net/problem/27496
# 24-06-03  python 3	112324 KB	412 ms  1틀렸습니다


def solution():
    answer = 0
    N, L = map(int, input().split())
    alcohols = list(map(int, input().split()))
    bac = 0
    
    def in_ballmer_peak(bac:int):
        return bac >= 129 and bac <= 138
    
    for t in range(L):
        bac += alcohols[t]
        if in_ballmer_peak(bac):
            answer += 1

    for t in range(L, N):
        bac += (alcohols[t] - alcohols[t-L])
        if in_ballmer_peak(bac):
            answer += 1
            
    return answer

print(solution())