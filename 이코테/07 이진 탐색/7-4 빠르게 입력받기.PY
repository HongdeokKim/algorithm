# 이진 탐색 문제는 입력 데이터가 많으므로 
# input()보다 sys 라이브러리의 readline() 함수를 사용

import sys
input_data = sys.stdin.readline().rsplit()
input_data_1 = sys.stdin.readline()

print(input_data)
print(input_data_1) # 개행까지
