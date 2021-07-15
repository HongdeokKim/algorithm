from sys import stdin
input = stdin.readline
print("\n".join(map(str, sorted([int(input()) for _ in range(int(input()))]))))
