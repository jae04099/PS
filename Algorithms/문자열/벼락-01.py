arr = ['  +--+-+-  ', '  +---+-+  ', '  +--+-+-  ', '  +-+-+-+  ']
result = []
for i in arr:
    i = i.strip().replace('+','1').replace('-','0')
    i = int(i, 2)
    i = chr(i)
    result.append(i)

result = ''.join(result)
print(result)
