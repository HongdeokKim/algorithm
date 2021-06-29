def solve():
    N, M = map(int, input().split())
    chess = input().split()
    print(chess)

    result_1 = 0
    result_2 = 0
    for i in range(0, N):
        for j in range(0, M):
            if (i + j) % 2 == 0: # 행, 열 index 합 짝수-W
                if chess[i][j] != 'W':
                    result_1 = result_1 + 1 # W가 아닌거
                else:
                    result_2 = result_2 + 1 # W였다 -> 두번째 케이스에서 틀린거
            else: # 홀수일때 B
                if chess[i][j] != 'B':
                    result_1 = result_1 + 1
                else:
                    result_2 = result_2 + 1 # B였다 -> 두 번째
    if result_1 < result_2:
        return result_1
    else:
        return result_2

print(solve())
