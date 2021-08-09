arr = [1, 3, 2, 4, 9, 5, 8, 6, 7, 0]

for i in range(len(arr)):
    min_index = i # index를 나타내는 것, 값X

    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
        # temp를 사용하지 않고 다음과 같이 스왑가능!
        arr[i], arr[min_index] = arr[min_index], arr[i] 

print(arr)