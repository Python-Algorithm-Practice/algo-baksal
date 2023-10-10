
""" [프로그래머스 PCCP 모의고사 #2] 실습용 로봇 """

def solution(command):
    answer = [0, 0]

    dir = 0     # 위 0 오른쪽 1 아래 2 왼쪽 3

    for c in command:
        
        if c == 'R':
            dir = moveR(dir)
        elif c == 'L':
            dir = moveL(dir)
        elif c == 'G':
            answer[0], answer[1] = moveG(answer[0], answer[1], dir)
        else:
            answer[0], answer[1] = moveB(answer[0], answer[1], dir)
    
    return answer

def moveR(dir):
    return (dir + 1) % 4

def moveL(dir):
    return 3 if dir-1 < 0 else dir-1

def moveG(x, y, dir):
    if dir == 0:
        return x, y+1
    elif dir == 1:
        return x+1, y
    elif dir == 2:
        return x, y-1
    else:
        return x-1, y

def moveB(x, y, dir):
    if dir == 0:
        return x, y-1
    elif dir == 1:
        return x-1, y
    elif dir == 2:
        return x, y+1
    else:
        return x+1, y


print(solution("GRGLGRG"))      # [2, 2]
print(solution("GRGRGRB"))      # [2, 0]