# 꿀 따기
# https://www.acmicpc.net/problem/21758

import sys
input = sys.stdin.readline


## 00.input
len_flowers = int(input())
flowers = list(map(int, input().split()))


## 01. sum : 100,000 x2
res_sum = [flowers[0]]
now = res_sum[0]
for ele in flowers[1:]:
    now += ele
    res_sum += [now]


## 03. Cases
answer = []
### 03-1. 벌벌꿀 (정방향)
temp = []
fixed = res_sum[-1] - res_sum[0]
for i in range(1, len_flowers):
    temp.append(res_sum[-1] - res_sum[i] - flowers[i])
answer.append(max(temp) + fixed)

### 03-2. 꿀벌벌 (역방향)
temp = []
fixed = (res_sum[-1] - res_sum[0]) - flowers[-1] + flowers[0]   # 정방향 결과 - 맨 뒤 + 맨 앞
for i in range(len_flowers -2, -1, -1):
    temp.append(res_sum[i] - res_sum[0] - flowers[i] + flowers[0] - flowers[i]) # 역방향 - 본인
answer.append(max(temp) + fixed)

### 03-3. 벌꿀벌
temp = []
for i in range(1, len_flowers - 1):
    temp.append((res_sum[i] - res_sum[0]) + (res_sum[-1] - res_sum[i] - flowers[-1] + flowers[i]))
answer.append(max(temp))

print(max(answer))