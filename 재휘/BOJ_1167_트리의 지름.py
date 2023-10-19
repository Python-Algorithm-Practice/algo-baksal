"""
DFS
(텍스트로만 설명하기 너무 힘들어요)
"""
import sys


def find_max_diameter(nodes, node, visit):
    visit[node] = True

    child_lines = []  # 각 자식 방향으로의 최대 길이 리스트
    two_line = 0  # 각 자식의 서브 트리 내에서 가장 긴 지름

    for child in nodes[node]:
        # 이미 방문한 곳이라면 패쓰
        if visit[child]:
            continue

        # child_line : 현재 노드에서 child를 쭉 타고 갔을 때 얻을 수 있는 최대 길이
        # max_line : child를 루트로 하는 서브 트리에서 가장 긴 지름 (완성품? 완성된 지름?)
        #
        child_line, max_line = find_max_diameter(nodes, child, visit)

        child_lines.append(child_line + nodes[node][child])
        two_line = max(two_line, max_line)  # max_line 갱신

    # 더 나아갈 수 없는 리프 노드일 경우 재귀 종료
    if not child_lines:
        return 0, 0

    # 가장 긴 줄을 찾기 위해 정렬
    child_lines.sort(reverse=True)

    # 자식이 둘 이상일 경우 아래에서 더 큰 값 선택
    # 자식의 서브 트리에서 완성된 지름
    # vs
    # 가장 긴 두 줄을 합쳐서 만든 지름
    if len(child_lines) >= 2:
        two_line = max(two_line, child_lines[0] + child_lines[1])

    return child_lines[0], two_line


def solution():
    sys_input = sys.stdin.readline

    v = int(sys_input())  # 노드 수 입력
    nodes = [dict() for _ in range(v + 1)]  # 노드 생성
    visit = [False] * (v + 1)  # 방문 배열 생성

    # 간선 정보 입력
    for _ in range(v):
        node, *edge_info = list(map(int, sys_input().split()))

        for i in range(1, len(edge_info), 2):
            nodes[node][edge_info[i - 1]] = edge_info[i]

    # 가장 긴 지름 찾기
    print(max(find_max_diameter(nodes, 1, visit)))


solution()
