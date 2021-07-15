# collections - Counter 사용, most_common 메서드 사용

from sys import stdin
from collections import Counter

input = stdin.readline
l = [int(input()) for _ in range(int(input()))]

print(round(sum(l) / len(l)))
l.sort()
print(l[len(l) // 2])
temp = Counter(l).most_common()
if len(temp) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])
print(max(l) - min(l))