# 뽑아내는건 list 안써도 됨

A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)