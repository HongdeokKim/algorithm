A, B, C = list(map(int, input().split()))
r = round(A / (C - B)) + 1

if r >= 1:
    print(r)
else:
    print(-1)
