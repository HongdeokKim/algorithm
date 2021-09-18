# 문제를 확실하게 이해해야함
# 가장 짧은 떡, 가장 긴 떡
# 왜 이진 탐색으로 문제를 풀어야 하는가
# 떡의 길이가 20억, 손님이 원하는 떡의 길이 10억

N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)

result = 0 # 임계점 mid
while start <= end:
    total = 0 # 자른 것의 총 길이
    mid = (start + end) // 2 
    for x in arr: # 전부 자르기
        if x > mid:
            total += x - mid
    if total < M: # 구해야하는 것보다 적으면 mid 내리기 -> end 내리기
        end = mid - 1
    else:
        result = mid # 현재의 결과 저장
        start = mid + 1 # 더 나은 것이 있는지 -> mid 올리기 -> start 올리기
print(result)