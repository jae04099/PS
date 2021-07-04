# 바이너리 서치
# data 중에서 target 을 검색하여 index 값을 return 한다.
# 없으면 None을 return한다.

data = [1, 5, 7, 13, 50, 120, 300, 320, 400, 700]

def binary_search(target, start, end, mid) :
    howMany = 0
    while start <= end:
        if data[mid] == target:
            howMany += 1
            return mid, howMany
        elif data[mid] < target:
            start = mid + 1
            howMany += 1
        else: 
            end = mid - 1
            howMany += 1
    return None, howMany

binary_search(300, 0, len(data) - 1, int(round(len(data) / 2, 0)))