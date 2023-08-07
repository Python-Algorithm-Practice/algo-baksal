# 프로그래머스 def solution(progresses, speeds):
#     answer = []
#
#     day = 1
#     cnt = 0
#     while progresses:
#         if progresses[0] + day * speeds[0] >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
#         else:
#             if cnt != 0:
#                 answer.append(cnt)
#                 cnt = 0
#             day += 1
#     answer.append(cnt)      # 마지막 cnt는 while문이 종료되어 else에서 answer에 append되지 않아 while문 종료후 append
#     return answer

def solution(progresses, speeds):
    answer = []

    day = 1
    cnt = 0
    while progresses:
        if progresses[0] + day * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt != 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)      # 마지막 cnt는 while문이 종료되어 else에서 answer에 append되지 않아 while문 종료후 append
    return answer