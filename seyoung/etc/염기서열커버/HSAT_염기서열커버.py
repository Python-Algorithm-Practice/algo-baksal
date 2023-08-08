"""
Q. 염기서열 커버
lv. 3
link: https://softeer.ai/practice/info.do?idx=1&eid=1526
--
못 풀어서 공식 해설봄
"""

import sys


def solution():
    WILDCARD = '.'

    def merge(dna1, dna2):
        if dna1 == [] or dna2 == []:
            return []
        dna = []
        for a, b in zip(dna1, dna2):
            if a == b or b == WILDCARD:
                dna.append(a)
            elif a == WILDCARD:
                dna.append(b)
            else:
                return []
        return dna

    def gen_superDNA(index):
        loc = 0
        temp_idx = index
        while temp_idx % 2 == 0:
            temp_idx //= 2
            loc += 1
        superDNA[index] = merge(DNA[loc], superDNA[index - 2 ** loc])

    def gen_answer(index):
        if answer[index] <= N:
            return answer[index]
        # 비트가 1인 위치 찾기
        bit1 = []
        number1 = number2 = 0  # number1 + number2 == index가 되도록 유지
        temp_idx = index
        for i in range(N):
            if temp_idx % 2 == 1:
                bit1.append(i)
                number2 += 2 ** i  # for문 종료 시, number2 == index
            temp_idx //= 2

        # 모든 부분집합에 대해 최소 answer 계산
        digit = [0] * len(bit1)  # 현재 bits
        for i in range(1, 2 ** (len(bit1) - 1)):
            for j in range(len(bit1)):
                if digit[j] == 1:
                    digit[j] = 0
                    temp = 2 ** bit1[j]
                    number1 -= temp
                    number2 += temp
                else:
                    digit[j] = 1
                    temp = 2 ** bit1[j]
                    number1 += temp
                    number2 -= temp
                    break
            temp = gen_answer(number1) + gen_answer(number2)

            if answer[index] > temp:
                answer[index] = temp
        return answer[index]

    # 입력
    N, M = map(int, input().split())
    DNA = [list(input()) for _ in range(N)]  # a c g t .

    # 초염기서열 생성: 비트가 1이면 커버된 DNA
    superDNA = [None for _ in range(2 ** N)]
    superDNA[0] = [WILDCARD] * M

    for i in range(1, 2 ** N):
        gen_superDNA(i)

    # 커버하기 위해 필요한 초염기서열 개수 계산
    answer = [N + 1] * (2 ** N)
    answer[0] = 0

    for i in range(1, 2 ** N):
        if superDNA[i] != []:
            answer[i] = 1
        else:
            gen_answer(i)

    print(answer[2 ** N - 1])


if __name__ == '__main__':
    solution()