# 연속 펄스 부분 수열의 합  level 3
# https://school.programmers.co.kr/learn/courses/30/lessons/161988

def solution(sequence):
    answer = 0
    # 연속 펄스 수열 누적합 만들기
    flag = -1
    pulse_prefix_sum = [sequence[0]]
    min_sum = min(0, pulse_prefix_sum[0])
    max_sum = max(0, pulse_prefix_sum[0])
    
    for i in range(1, len(sequence)):
        pulse_prefix_sum.append(pulse_prefix_sum[-1] + sequence[i] * flag)
        flag *= -1
        
        min_sum = min(min_sum, pulse_prefix_sum[i])
        max_sum = max(max_sum, pulse_prefix_sum[i])
    return abs(max_sum - min_sum)