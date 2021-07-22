A, B = list(map(str, input().split()))

A = list(A)
A.sort(reverse=True)
B = list(B)
B.sort(reverse=True)
A = int("".join(A))
B = int("".join(B))
if  A > B:
    print(A)
else:
    print(B)