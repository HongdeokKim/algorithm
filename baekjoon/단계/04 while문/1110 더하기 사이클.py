from sys import stdin
input = stdin.readline

cnt = 0
N = int(input())
a = N // 10
b = N %  10
newN = b * 10 + (a + b) % 10
while True:
    if N == newN:
        break
    else:
        a = newN // 10
        b = newN %  10
        newN = b * 10 + (a + b) % 10
        cnt += 1
print(cnt + 1)