A, B = list(map(str, input().split()))

A = list(A)
A.reverse()
B = list(B)
B.reverse()
A = int("".join(A))
B = int("".join(B))
if  A > B:
    print(A)
else:
    print(B)

'''
a, b =input().split()

def reading(k):
    k = k[::-1]
    print(k)
    return int(k)

print(max([reading(a),reading(b)]))
'''