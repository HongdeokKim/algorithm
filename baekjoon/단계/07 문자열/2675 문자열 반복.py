T = int(input())
l = []

for _ in range(T):
    l.append(input().split())

for R, S in l:
    for s in S:
        print(int(R)*s, end="")
    print()