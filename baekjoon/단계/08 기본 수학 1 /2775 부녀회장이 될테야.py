T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    l = [[i for i in range(1, n+1)]]

    for i in range(1, k):
        l.append([sum(l[j][:j]) for j in range(1, n)])
    print(l)
    