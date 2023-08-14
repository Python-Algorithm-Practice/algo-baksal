
""" [프로그래머스] Level 2. 프로세스 """

def solution(priorities, location):
    answer = 0

    P = [(pr, idx) for idx, pr in enumerate(priorities)]  
    N = len(priorities) - 1  

    # while len(P) > 1:
    while answer < N:
        
        temp = P.pop(0)

        if temp[0] < max(P)[0]:
            P.append(temp)
            continue
        
        answer += 1

        if temp[1] == location:
            break
    
    else:
        answer += 1

    return answer

print(solution([2, 1, 3, 2], 2))            # 1
print(solution([1, 1, 9, 1, 1, 1], 0))      # 5

print(solution([1, 1, 1, 2], 2))            # 4