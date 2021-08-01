l = []

while True:
    N = int(input())
    if N == 0:
        break
    l.append(N)

M = max(l) * 2 + 1
s = [True] * M

for i in range(2, int(M**(1/2)) + 1):
    if s[i]:
        for j in range(2*i, M, i):
            s[j] = False

for i in l:
    if i == 1:
        print(1)
    else:
        cnt = 0
        for j in range(i+1, 2*i+1):
            if s[j] == True:
                cnt += 1
        print(cnt)

# 더 깊은 알고리즘 방식을 알아야함
# 780ms -> 88ms
# 홀수만 찾기, 이진 분할 알고리즘..?