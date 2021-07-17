from sys import stdin
input = stdin.readline
l = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    l.append([a, b])

for idx, data in enumerate(l):
    print("Case #%d: %d + %d = %d" % (idx + 1, data[0], data[1], data[0] + data[1]))
