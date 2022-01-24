# 너비 우선 탐색

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # deque에 입력받은 노드를 넣어줌
    visited[start] = True

    while queue: # Queue가 없을 때까지 반복
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i) # 방문하지 않은 노드라면 Queue에 추가
                visited[i] = True # DFS와 다르게 반복문이기에 살짝 다름

graph = [
    [],
    [2, 3, 8], # graph[1]은 2, 3, 8 노드와 연결되어있음
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)