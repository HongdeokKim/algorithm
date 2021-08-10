arr = [1, 3, 2, 4, 9, 5, 8, 6, 7, 0]

def quick_sort(arr, start, end):
    if start >= end:
        pivot = start
        left  = start + 1
        right = end

        while left <= right:
            while