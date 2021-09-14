from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 움직이는 것 정의, index로 사용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 첫 번째 Queue에 넣고

    while queue: # Queue가 빌때까지 반복
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]

print(bfs(0, 0))    

# dfs와 bfs를 다뤄봄
# 많은 문제를 풀어봐야겠다
# 움직임 리스트를 만드는 것
# 탈락 조건을 만드는 것
# 최단거리를 그래프에 직접 저장하는 것