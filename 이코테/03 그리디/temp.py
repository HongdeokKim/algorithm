n = 1260
cnt = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    cnt += n // coin
    n %= coin # % 연산: 나머지만 남음

print(cnt)