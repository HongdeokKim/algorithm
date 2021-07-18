from sys import stdin
input = stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(*(input().split()))
for s in l:
    plus_sig = 0
    score = 0
    for c in s:
        if plus_sig and c == 'O':
            score += 1 + plus_sig
            plus_sig += 1
        elif (not plus_sig) and c == 'O':
            plus_sig = 1
            score += 1
        else:
            plus_sig = 0
    print(score)
    
# 굳이 세가지로 안나눠도 될 것 같다
'''
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)
    '''