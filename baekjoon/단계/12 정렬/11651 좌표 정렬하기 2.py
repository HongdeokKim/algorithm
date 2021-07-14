from sys import stdin

input = stdin.readline
l = [input() for _ in range(int(input()))]
l.sort(key=lambda a: (int(a.split()[1]), int(a.split()[0])))
print("".join(l))