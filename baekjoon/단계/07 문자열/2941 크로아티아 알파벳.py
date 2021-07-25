# 풀이를 보고 아이디어를 배움

ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in ca:
    # replace 함수는 (old, new)를 바꾸고 return한다
    # 글자의 갯수를 구하는것에 초점을 둔다
    s = s.replace(i, '*')

print(len(s))

# 코드의 규칙을 파악하는 코드
# 길이를 구해서 조건에 맞으면 빼는 방식
# 나올수있는 경우를 전부 예측
# 문자열 더하는 + 연산자 사용
'''
x = input()
y = len(x)
cro_al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in range(0, len(x)):
    if len(x) < 2:
        y = len(x)
    elif len(x) == 2:
        if (x[i-2] + x[i-1]) in cro_al:
            y = 1
    elif (x[i-3]+x[i-2]+x[i-1]) in cro_al:
        y -= 2
    elif (x[i-2] + x[i-1]) in cro_al:
        y -= 1
print(y)
'''