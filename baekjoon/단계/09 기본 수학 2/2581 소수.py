M = int(input())
N = int(input())
l = list(range(M, N + 1))

for i in range(M, N + 1):
    if i == 1:
        l.remove(i)
        continue
    for j in range(2, i):
        if i % j == 0:
            l.remove(i)
            break
if l == []:
    print(-1)
else:
    print(sum(l))
    print(min(l))


