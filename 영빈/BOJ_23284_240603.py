# 모든 스택 수열    gold 5
# https://www.acmicpc.net/problem/23284
# 24-06-03  Python 3    38828 KB	208 ms
#           Pypy 3      127888 KB	432 ms

from typing import List


def solution():
    n = int(input())
    

    def recursion(stack: List[int], sequence: List[int], next_num: int):
        if next_num == n:   # 마지막 숫자가 나오면 걜 스택에 넣든 수열에 바로 넣든 결과가 같으므로 바로 print 해준다.
            stack_sequence = []
            stack_sequence.extend(sequence)
            stack_sequence.append(n)
            stack_sequence.extend(reversed(stack))
            return print(*stack_sequence)
        
        # 1. 현재 숫자를 수열에 바로 넣는 경우
        sequence.append(next_num)
            # 1-1. stack에 있던 숫자들을 사용한다
        popped_stack = []
        pushed_sequence = [elem for elem in sequence]
        pushed_sequence.extend(reversed(stack)) # stack에 있던 숫자는 모두 현재 숫자보다 작으므로, 많이 쓸 수록 사전 순서 상 앞
        for _ in range(len(stack)):
            recursion(popped_stack, pushed_sequence, next_num + 1)
            popped_stack.append(pushed_sequence.pop())
            # 1-2. stack에 있던 숫자들을 사용하지 않는다 (사전 순으로 밀림)
        recursion(stack, sequence, next_num + 1)
        sequence.pop()

        # 2. 현재 숫자를 stack에 넣는 경우: 뒷 숫자를 먼저 넣게 된다 (사전 순으로 밀림)
        stack.append(next_num)
        recursion(stack, sequence, next_num + 1)
        stack.pop()
    
    recursion([], [], 1)

solution()