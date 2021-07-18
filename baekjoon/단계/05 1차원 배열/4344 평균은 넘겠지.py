from sys import stdin
input = stdin.readline

C = int(input())
avg = []
for _ in range(C):
    l = list(map(int, input().split()))
    N = l[0]
    l.pop(0)
    m = sum(l) / N
    cnt = 0
    for i in l:
        if i > m:
            cnt += 1
    avg.append(cnt / N)
for i in avg:
    print("%.3f%%" % (i*100))


