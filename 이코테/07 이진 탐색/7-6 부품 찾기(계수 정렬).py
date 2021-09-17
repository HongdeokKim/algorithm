n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1 # 물건이 인덱스, 1은 있다는 의미

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")

# input의 범위가 정해져있으므로 계수를 통해 바로 접근이 가능