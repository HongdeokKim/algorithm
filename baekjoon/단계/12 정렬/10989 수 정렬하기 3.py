import sys
n = int(input())
check_ls = [0] * 10001 # 카운팅 수

for _ in range(n):
    num = int(sys.stdin.readline())
    check_ls[num] = check_ls[num] + 1 # 값을 인덱스로 접근하여 카운팅

for i in range(10001):
    if check_ls[i] != 0:
        for _ in range(check_ls[i]): # 여러개일수있음
            print(i)