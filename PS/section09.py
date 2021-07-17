# 파일 읽기, 쓰기
# 읽기: r. 쓰기(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a

# 파일 읽기
f = open('../../review.txt', 'r')
content = f.read()
print(content)

# 반드시 close로 리소스 닫아야함
f.close()

#----------------------------------
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)

#====================================
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

#====================================
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용 없음
    print(">", content)

#====================================
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' ')
        line = f.readline()
