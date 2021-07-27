N = int(input())
num = 1
cnt = 1
while N > num:
    num += 6 * cnt
    cnt += 1
print(cnt)
'''
2~7
8~19
20~37
'''

# print(int(-(-(3+(12*int(input())-3)**.5)//6)))