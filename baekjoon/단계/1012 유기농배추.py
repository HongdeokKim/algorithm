from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    l = [[0] * M] * N

    print(l)
    for _ in range(K):
        x, y = map(int, input().split())
        l[y][x] = 1

    for i in range(N):
        for j in range(M):
            print(l[j][i], end=" ")
        print()


# def find():
