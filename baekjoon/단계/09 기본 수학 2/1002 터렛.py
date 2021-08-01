N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    
    if r == 0 and r1 == r2:
        print(-1) # 원이 겹칠때
    elif abs(r1 - r2) == r or r1 + r2 == r:
        print(1) # 원이 내접, 외접일때
    elif abs(r1 - r2) < r < (r1 + r2):
        print(2) # 원이 서로다른 두 점에서 만날 때
    else:
        print(0)
    
# abs 절댓값 함수