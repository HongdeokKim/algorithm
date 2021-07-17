# 이해를 못했음

N = int(input())

def solve(n, start, end):
    if n > 1:
        solve(n-1, start, 6-start-end)
    print(start, end)
    if n > 1:
        solve(n-1, 6-start-end, end)
print(2**N-1)
solve(N, 1, 3)
