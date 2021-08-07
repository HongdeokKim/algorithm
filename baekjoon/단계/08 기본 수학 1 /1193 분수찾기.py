

def find_index(N):
    n = 1
    while n * (n + 1) / 2 < N:
        n += 1

    temp = N - ((n-1) * n) / 2
    print(temp)
    print(n)
    if n % 2 == 0: # 짝수
        print("%d/%d" % (1 + temp, n + 1 - temp))
    else: # 홀수
        pass
    
    

    return n

while True:
    N = int(input())
    find_index(N)
'''
0 0

1 0
0 1

n(n + 1) < 28

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