M, N = map(int, input().split())
N += 1
s = [True] * N

for i in range(2, int(N**(1/2)) + 1):
    if s[i]:
        for j in range(2*i, N, i):
            s[j] = False

for i in range(M, N):
    if 1 < i and s[i]:
        print(i)

# 에라토스테네스의 체
# for문 -> i배, 3번째 인자
# 2번째 for문 시작은 2*i부터
# 리스트 s, 체-틀 사용