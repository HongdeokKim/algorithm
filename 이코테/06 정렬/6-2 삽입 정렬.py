arr = [1, 3, 2, 4, 9, 5, 8, 6, 7, 0]

for i in range(1, len(arr)):
    for j in range(i, 0, -1): # 거꾸로 할때는 range 반대로 쓴다
        if arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break # 자기보다 작은 값을 만나면 정지
print(arr)