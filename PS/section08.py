# import datetime
# now = datetime.datetime.now()
# print(now)

# 파이썬의 자료형인 리스트, 딕셔너리 등은 기초적인 자료구조인 배열, 해시테이블 등을 사용하기 좋게 잘 구현한 구현체.
# 이미 더 고차원적인 자료형을 파이썬에서 제공하고 있는 것이기 때문에, 대부분 자료구조는 파이썬의 자료형을 이용하면 쉽게 구현이 가능
# 그럼에도 자료구조 학습에 이러한 방식을 쓰지 않는 이유는, 원리적인 내용을 이해하기 위함
# 자료구조 배열: 단순히 연속된 메모리 공간
# 공간을 예약한다는 것은 배열로 사용될 메모리 공간을 할당하는 것. 메모리 할당이 배열의 단점이 되는 이유는 메모리를 작게 잡을 경우 메모리가 부족해서 다시 잡아야하는 경우가 생기고, 크게 잡을 경우 메모리 낭비가 발생하기 때문임

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(self.name + ' cannot speak.')

#     def move(self):
#         print(self.name + ' cannot move.')


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name

#     def move(self):
#         print(self.name + ' moves like a jagger.')


# class Retriever(Dog):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name

#     def move(self):
#         super().move()

#     def speak(self):
#         print(self.name + ' is smart enough to speak')


# dog = Dog('Nancy')
# dog.speak()
# dog.move()

# super_dog = Retriever('Michael')
# super_dog.speak()
# super_dog.move()

# class Median:
#     def __init__(self):
#         self.itemList = []
#         self.finResult = float()

#     def get_item(self, item):
#         self.itemList.append(item)

#     def clear(self):
#         self.itemList = []

#     def show_result(self):
#         if self.itemList[-1] == len(self.itemList) - 1:
#             return None
#         elif len(self.itemList) % 2 == 0:
#             self.finResult = (self.itemList[len(
#                 self.itemList) // 2 - 1] + self.itemList[len(self.itemList) // 2]) // 2
#             print(self.finResult)
#         else:
#             self.finResult = self.itemList[len(self.itemList) // 2]
#             print(self.finResult)


# median = Median()
# for x in range(10):
#     median.get_item(x)
# median.show_result()

# median.clear()
# for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
#     median.get_item(x)
# median.show_result()

class Foo():
    bar = 'A'
    def __init__(self):
        self.bar = 'B'
    class Bar():
        bar = 'C'
        def __init__(self):
            self.bar = 'D'

print(Foo.bar)       
print(Foo().bar)     
print(Foo.Bar.bar)   
print(Foo.Bar().bar)