# l = []
# cnt = 0

# N, M = map(int, input().split())
# for _ in range(N):
#     l.append(input())

# table = [[False] * M] * N


# for i in range(N):
#     for j in range(M):
#         table[N][M] = True

#         if table[N][j] == False and l[N][M] == '0':
            

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] == 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)

