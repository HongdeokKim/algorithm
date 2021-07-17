from sys import stdin
input = stdin.readline
l = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        l.append(str(A + B))
print("\n".join(l))
