from sys import stdin
input = stdin.readline
l = []
p = []
while True:
    l = list(map(int, input().split()))
    if l[0] == l[1] == l[2] == 0:
        break
    l.sort()
    if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
        p.append("right")
    else:
        p.append("wrong")
print("\n".join(p))