A, B, C = list(map(int, input().split()))
r = round(A / (C - B)) + 1

if r < 0:
    print(-1)
else:
    print(r)