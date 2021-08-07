N = int(input())
n = 1
while n * (n + 1) / 2 < N:
    n += 1

temp = N - ((n - 1) * n / 2) - 1

if n % 2 == 0: # 짝수
    print("%d/%d" % (1 + temp, n - temp))
else: # 홀수
    print("%d/%d" % (n - temp, 1 + temp))