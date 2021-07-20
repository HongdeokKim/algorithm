# chr 함수 -> 숫자를 아스키문자로
s = input()
for i in range(97, 123):
    print(s.find(chr(i)), end=" ")