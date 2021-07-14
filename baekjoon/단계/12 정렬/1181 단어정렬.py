from sys import stdin, stdout

N = int(stdin.readline())
l = []

for i in range(N):
    word = stdin.readline().strip()
    # list는 mutable합니다. 따라서 hash로 처리할 수 없고, 
    # 따라서 set 함수를 이용해서 처리할 수 없는 것이죠.
    # 튜플로 처리
    l.append((word, len(word))) 

l = list(set(l))
l.sort(key= lambda a: (a[1], a[0]))

for i in l:
    stdout.write(i[0]+ "\n")

# 굳이 이거 안해도, 그냥 sort하고 len->sort하면 이름, 길이 됨