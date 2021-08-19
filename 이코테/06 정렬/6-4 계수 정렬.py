arr = [1, 3, 2, 4, 9, 5, 8, 6, 7, 0]

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')