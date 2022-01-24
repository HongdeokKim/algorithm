from collections import deque
from sys import stdin
input = stdin.readline

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, v, visited):
    visited = [False] * (N + 1)
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = []
for _ in range(N + 1):
    graph.append([])
visited = [False] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


DFS(graph, 1, visited)
print()
BFS(graph, 1, visited)