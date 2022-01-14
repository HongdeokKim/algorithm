from sys import stdin
input = stdin.readline

l = []
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        l.append(n)
    else:
        l.pop()
print(sum(l))