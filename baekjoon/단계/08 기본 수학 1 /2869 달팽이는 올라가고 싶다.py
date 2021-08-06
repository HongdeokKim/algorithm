import math

A, B, V = map(int, input().split())

print(math.ceil((V - A) / (A - B) + 1))

# math 라이브러리를 안쓰고 +.99 -> int()를 통해 같은 역할을 수행할 수 있음