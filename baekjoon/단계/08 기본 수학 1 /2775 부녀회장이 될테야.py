T = int(input())
s = []

for _ in range(T):
    k = int(input())
    n = int(input())

    l = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            l[j] = l[j - 1] + l[j]
    s.append(l[n - 1])

print("\n".join(map(str, s)))
    