lists = [1, 8, 6, 2, 5, 4, 8, 3, 7]
left = 0
right = len(lists) - 1
result = 0

for i in range(len(lists)):
    while(right - left >= 0):
        result = max(result, min(lists[left], lists[right]) * (right - left))

        if lists[right] < lists[left]:
            right -= 1 
        else:
            left += 1
print(result)