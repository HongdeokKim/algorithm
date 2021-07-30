A, B, V = map(int, input().split())

h = A # 낮
w = A - B
day = 1
while h < V:
    h += w # 밤
    day += 1
print(day)
