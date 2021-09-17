n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

N.sort()
for i in M:
    if bin_search(N, i, 0, n - 1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
