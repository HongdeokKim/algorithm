'''
from sys import stdin
input = stdin.readline

cnt = 0
temp = None
s = set()

for _ in range(int(input())):
    for i in input().rstrip():
        if i != temp and i in s:
            cnt -= 1
            break
        else:
            s.add(i)
            temp = i
    cnt += 1
    s.clear()
print(cnt)
'''

        
result = 0
for i in range(int(input())):
    word = input()
    print(list(word))
    print(sorted(word, key=word.find))
    print(sorted(word))
    print(word.find)
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)


# 연속안되는 경우
# 이미 set에 단어가 있음
# 그런데 temp가 있다면 제외

