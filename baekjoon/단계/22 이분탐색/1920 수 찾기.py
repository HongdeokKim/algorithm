N = int(input())
A = list(map(int, input().split()))
M = int(input())
test = list(map(int, input().split()))

A.sort() # 정렬

for num in test:
    start, end = 0, N-1
    mid = (start + end) // 2

    while True:
        #print("시도")
        if start > end:
            #print("미발견")
            print(0)
            break

        #print(num, start, end, mid, A[mid])
        if A[mid] > num:
            #print("작게 가자")
            end = mid - 1
            mid = (start + end) // 2
        elif A[mid] < num:
            #print("크게 가자")
            start = mid + 1
            mid = (start + end) // 2
        else:
            #print("찾았네")
            print(1)
            break