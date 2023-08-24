def solution(bridge_length, weight, truck_weights):
    answer = 0

    b = [0] * bridge_length  # 다리 배열
    t = 0
    while b:
        t += 1
        b.pop(0)

        if truck_weights:
            # 다리가 트럭의 무게들을 버티면 트럭통과
            if sum(b) + truck_weights[0] <= weight:
                b.append(truck_weights.pop(0))
                # 아니면 트럭 대기
            else:
                b.append(0)
    return t