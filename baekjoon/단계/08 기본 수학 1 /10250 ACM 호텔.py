T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    if N & H == 0:
        print((N % H) * 100 + H)
    else:
        print((N % H) * 100 + (N // H) + 1)

