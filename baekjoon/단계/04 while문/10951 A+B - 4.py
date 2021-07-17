# try와 except를 사용함

from sys import stdin
input = stdin.readline
while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    print(A + B)