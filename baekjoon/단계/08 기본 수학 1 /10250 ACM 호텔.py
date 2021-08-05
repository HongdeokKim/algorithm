T = int(input())
l = []

for _ in range(T):
    H, W, N = map(int, input().split())
    temp = (N // H) + 1

    if temp < 10:
        l.append(str(N % H) + "0" + str(temp))
    else:
        l.append(str(N % H) + str(temp))
   
print("\n".join(l))

