T = int(input())
l = []
s = [True] * 10000

for _ in range(T):
    l.append(int(input()))

for i in range(2, 101):
    if s[i]:
        for j in range(2*i, 9999, i):
            s[j] = False

for i in l:
    if i % 2 == 0:
        l, r = int(i / 2), int(i / 2)
    else:
        l, r = int(i / 2), int(i / 2) + 1
    while True:
        if s[l] and s[r]:
            print(l, r)
            break
        else:
            l -= 1
            r += 1

'''
from sys import stdin
input = stdin.readline

T = int(input())
answer = ""
result = [False, False, True] + [True, False] * 5000
for number in range(3, 101, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
        # 원하는 index에 False를 넣는 방법

for tc in range(T):
    N = int(input())
    if N == 4:
        answer += "2 2\n"
        continue
    harf_N = N//2
    if not harf_N % 2:
        harf_N += 1
    for i in range(harf_N, N, 2):
        if result[i] and result[N-i]:
            answer += "{} {}".format(N - i, i) + "\n"
            break
print(answer, end="")
'''