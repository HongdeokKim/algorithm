T = int(input())
l = []
for i in range(T):
    l.append(sum((map(int, input().split()))))
for i in range(T):
    print("Case #%d: %d" % (i + 1, l[i]))