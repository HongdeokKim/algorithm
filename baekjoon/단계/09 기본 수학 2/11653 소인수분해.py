N = int(input())
l =[]

while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            N = N // i
            l.append(i)
            break
        
print("\n".join(map(str, l)))