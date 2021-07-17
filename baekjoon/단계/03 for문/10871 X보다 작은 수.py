_, X = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    if(i < X):
        print(i, end=" ")
        
# 방법
# score = [x for x in input().split() if int(x)<b]
