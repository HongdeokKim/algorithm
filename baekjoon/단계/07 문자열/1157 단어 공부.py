l = input()
l.upper()
a = {}

for i in l.upper():
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

#a = sorted(a.items)
a = sorted(a.items(), key=lambda a: a[1], reverse= True)

if len(a) == 1:
    print(a[0][0])
elif a[0][1] == a[1][1]:
    print("?")
else:
    print(a[0][0])

# 별로 좋아하지 않는 코드