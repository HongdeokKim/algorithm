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