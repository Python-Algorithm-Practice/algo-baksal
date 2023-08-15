
""" [백준] 골드 5. 두 용액 """

import sys

N = int(sys.stdin.readline())                       # 전체 용액의 수
S = list(map(int, sys.stdin.readline().split()))    # 각 용액의 특성값

S.sort()

start = 0
end = N-1

answer = sys.maxsize
number = ()

while start < end:

    sum = S[start] + S[end]

    if abs(sum) < answer:
        answer = abs(sum)
        number = (S[start], S[end])
    
    if sum < 0:
        start += 1
    else:
        end -= 1

print(number[0], number[1])