from sys import stdin

N = int(stdin.readline())
l = []
for i in range(N):
    l.append(list(map(int, stdin.readline().split())))
l.sort()
for i in l:
    print(i[0], i[1])

