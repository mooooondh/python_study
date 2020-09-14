# dijkstra01.py
# 다익스트라 알고리즘. 구현 쉽고, 속도 느린 버전

import sys

input= sys.stdin.readline
INF= int(1e9)

n, m= map(int, input().split()) # 노드의 갯수, 간선의 갯스
start= int(input()) # 시작 노드
graph= [[] for _ in range(n+ 1)]    # 노드 연결정보
visited= [False]* (n+ 1)    # 방문기록
distance= [INF]* (n+ 1)   # 최단거리 리스트

for _ in range(m):
    a, b, c= map(int, input().split())  # a에서 b로 가는 비용은 c
    graph[a].append((b, c))

def get_smallest_node():
    min_val= INF
    index= 0
    for i in range(1, n+ 1):
        if (distance[i]< min_val and not visited[i]):
            min_val= distance[i]
            index= i

    return index

def dijkstra(start):
    distance[start]= 0
    visited[start]= True

    for j in graph[start]:
        distance[j[0]]= j[1]

    for i in range(n- 1):
        now= get_smallest_node()
        visited[now]= True
        for j in graph[now]:
            cost= distance[now]+ j[1]
            if (cost< distance[j[0]]):
                distance[j[0]]= cost

dijkstra(start)

print("graph: ", graph)
print("visited: ", visited)
print("distance: ", distance)

for i in range(1, n+ 1):
    if (distance[i]== INF):
        print("INFINITY")
    else:
        print(distance[i])