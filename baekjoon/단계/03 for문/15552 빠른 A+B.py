# 입출력 효율성에 관한 문제
# 중요하게 생각해볼 필요가 있음

import sys

N = int(sys.stdin.readline())
l = []

for i in range(N):
    l.append(list(map(int, sys.stdin.readline().split())))
for i in l:
    print(i[0] + i[1])

'''
import sys
io = sys.stdin.read().split('\n')
T = int(io[0])
del io[0]

for i in range(T):
  A,B = io[i].split()
  io[i] = (f"{int(A)+int(B)}\n")

sys.stdout.write(''.join(io))
'''