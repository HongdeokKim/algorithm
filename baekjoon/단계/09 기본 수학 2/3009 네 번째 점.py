l, r = [], []

for _ in range(3):
    x, y = map(int, input().split())

    if x in l:
        l.remove(x)
    else:
        l.append(x)
    if y in r:
        r.remove(y)
    else:
        r.append(y)
print(*l, *r)