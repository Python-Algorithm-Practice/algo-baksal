
""" [백준] 골드 4. 타일 채우기 """

def solution():
    
    N = int(input())

    # 홀수는 채울 수 없음
    if N % 2 == 1:
        return 0
    
    table = {2:3}   # 초기 설정

    # 4의 경우 = [2] * 3 + 2                        = 11
    # 6의 경우 = [4] * 3 + [2] * 2 + 2              = 41
    # 8의 경우 = [6] * 3 + [4] * 2 + [2] * 2 + 2    = 153 (123 + 22 + 6 + 2)
    # ...

    for i in range(4, N+1, 2):
        count = table[i-2] * 3          # 2열을 만드는 경우의 수가 3개 -> 이전에 만들어진 경우의 수 * 2열을 만드는 경우의 수 (3)
        for j in range(i-4, 0, -2):
            count += table[j] * 2       # 독특한 패턴을 활용하는 경우의 수 (2)
        table[i] = count + 2            # 항상 독특한 패턴이 2개 생김

    return table[N]

print(solution())