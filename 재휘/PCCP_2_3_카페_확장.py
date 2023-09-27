"""

"""


def get_time_table(menu, order, k):
    # 입장 시각 설정
    time_table = [[idx * k, None] for idx in range(len(order))]

    # 퇴장 시각 설정
    time_table[0][1] = menu[order[0]]  # 첫 사람 음료는 주문 직후 제조하므로 냅다 설정해 버리기
    for idx in range(1, len(order)):
        # idx 번째 사람의 입장 시각과 직전 사람의 퇴장 시각 중 더 늦는 시각을 기준으로 하기
        time_table[idx][1] = max(
            time_table[idx - 1][1],
            time_table[idx][0]
        ) + menu[order[idx]]

    return time_table


def get_personnel(time_table):
    # 시간별 초기 데이터를 0명으로 설정
    personnel = [0] * (time_table[-1][1] + 2)

    # 누적합 배열 초기 설정
    for enter_time, exit_time in time_table:
        personnel[enter_time] += 1
        personnel[exit_time] -= 1

    # 쭉쭉 반영해 나가기
    for time in range(1, len(personnel)):
        personnel[time] += personnel[time - 1]

    return personnel


def solution(menu, order, k):
    # 입장 및 퇴장 시각 시간표 만들기
    time_table = get_time_table(menu, order, k)

    # 시간별 입장 인원 구하기
    personnel = get_personnel(time_table)

    # 최대 인원 반환
    return max(personnel)


print(solution([5, 12, 30], [1, 2, 0, 1], 10))
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))
