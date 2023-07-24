
""" 골드 5. A와 B 2 """

s = input()     # 시작 문자열
t = input()     # 최종 문자열

def doCheck(n):   

    if len(n) <= len(s):
        if n == s:
            print(1)
            exit(0)
        return
    
    if n[-1] == 'A':            # 문자열의 뒤에 A를 추가한다.
        doCheck(n[:-1])
    
    if n[0] == 'B':             # 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
        temp = n[1:]
        doCheck(temp[::-1])

doCheck(t)
print(0)