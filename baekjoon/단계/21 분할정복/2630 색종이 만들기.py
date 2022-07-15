from sys import stdin
input = stdin.readline

N = (int(input()))
P = []
blue  = 0
white = 0

for _ in range(N):
    P.append(list(map(int, input().split())))

def find(x, y, size):
    global blue, white
    color = P[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if P[i][j] != color:
                find(x, y, size // 2)
                find(x, y + size // 2, size // 2)
                find(x + size // 2, y, size // 2)
                find(x + size // 2, y + size // 2, size // 2)
                return
    if color == 0:
        white = white + 1
        return
    else:
        blue = blue + 1
        return

find(0, 0, N)
print(white)
print(blue)