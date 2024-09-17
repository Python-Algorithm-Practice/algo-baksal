import sys
input = sys.stdin.readline

INF = int(1e9)
len_test_cases = int(input())

for test_case in range(len_test_cases):
    ## 00. Input data
    len_nodes, len_roads, len_warms = map(int, input().split())
    road_graph = [[INF] * (len_nodes + 1) for _ in range(len_nodes + 1)]
    
    ## 01. road graph
    for i in range(len_roads):
        here, there, cost = map(int, input().split())
        road_graph[here][there] = road_graph[there][here] = min(road_graph[here][there], cost)

    ## 02. warm-hole graph
    for i in range(len_warms):
        here, there, rewind = map(int, input().split())
        road_graph[here][there] = -1 * rewind

    ## 02. Floyd-Warshall
    for via in range(1, len_nodes + 1):
        for here in range(1, len_nodes + 1):
            for there in range(1, len_nodes + 1):
                road_graph[here][there] = min(road_graph[here][there], road_graph[here][via] + road_graph[via][there])

    ## 03. Warm-hole check
    answer = "NO"
    for i in range(1, len_nodes + 1):
        if road_graph[i][i] < 0:
            answer = "YES"
            break
            
    print(answer)