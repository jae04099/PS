돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
stone_length = len(돌의내구도)

독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]
result = []

for i in range(len(독)):
    now_dog = 독[i]
    now_location = int(now_dog['점프력'])
    while stone_length >= now_location:
        if int(now_dog['몸무게']) > 돌의내구도[now_location - 1]:
            break
        else:
            돌의내구도[now_location - 1] -= int(now_dog['점프력'])
            now_location += int(now_dog['점프력'])
            continue
    if stone_length <= now_location:
        result.append(독[i]['이름'])
print("생존자 : ", result)


