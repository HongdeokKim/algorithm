s = input()
t = 0
for i in s:
    i = ord(i)
    if 65 <= i <= 67:
        t += 3
    elif 68 <= i <= 70:
        t += 4
    elif 71 <= i <= 73:
        t += 5
    elif 74 <= i <= 76:
        t += 6
    elif 77 <= i <= 79:
        t += 7
    elif 80 <= i <= 83:
        t += 8
    elif 84 <= i <= 86:
        t += 9
    elif 87 <= i <= 90:
        t += 10
print(t)

'''
1 - 2
2 - 3
3 - 4
..

9 2
10 3
'''