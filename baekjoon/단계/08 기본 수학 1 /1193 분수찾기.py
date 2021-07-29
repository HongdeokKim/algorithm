N = int(input())
n = 1
cnt = 1
while cnt < N:
    n += 1
    cnt += n
print(n, cnt)

n -= 1
cnt -= 1

if n % 2 == 0:
    pass
else:
    pass

'''
0 0

1 0
0 1

0 2
1 1
2 0

3 0
2 1
1 2
0 3

0 4
1 3
2 2
3 1
4 0

'''