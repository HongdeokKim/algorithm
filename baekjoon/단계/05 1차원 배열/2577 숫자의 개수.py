N = 1
for _ in range(3):
    N *= int(input())
N = str(N)
for i in range(10):
    print(N.count(str(i)))