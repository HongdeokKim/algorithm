import sys

N = int(sys.stdin.readline())
l = []

for i in range(N):
    l.append(list(map(int, sys.stdin.readline().split())))
for i in l:
    print(i[0] + i[1])
