# 파이썬 클래스
# 선언

class UserInfo:
    def __init__(self, name):
        self.name = name

    def user_info(self):
        print("Name : ", self.name)


# user1은 객체, user1은 UserInfo의 인스턴스
user1 = UserInfo('lena')
user1.user_info()

# self란
# class SelfTest:
#     def funtion1():
#         print('function1 called!')
#     def funtion2(self):
#         print('function2 called!')

# self_test = SelfTest()
# self_test.function1()   # error

# 상속


class JSS:
    def __init__(self):
        self.name = input("name:")
        self.age = input("age:")

    def show(self):
        print("my name is {}".format(self.name))


class JSS2(JSS):
    def __init__(self):
        super().__init__()  # self.name, self.age 다 상속됨
        self.gender = input("gender:")

# 자기 인스턴스 안에 변수가 없으면 클래스로 넘어가서 글로벌 변수를 확인해본다. 그래도 없으면 에러.

# ------------------------------------------------------------
# 상속 다중상속
# 슈퍼클래스(부모), 서브클래스(자식) -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        return 'Car Info : %s %s %s' % (self.name, self.color, self.type)
        # 자식에 super().show()라고 하면 메소드 복사됨


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)


class Foo:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('i am' + self.name)
class Bar(Foo):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print('you are' + self.name)

bar = Bar('John')
bar.speak()

# method overriding
# 자식이 부모와 같은 이름의 메소드를 만들어 호출한다면 자식의 것에 오버라이딩됨
model2 = BenzCar()

#  parent method call

# mro()는 상속 관계를 알려준다
print(BmwCar.mro())
print(BenzCar.mro())

# 다중상속

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X, Y):
    pass

class B(Y, 2):
    pass

class M(B, A, Z):
    pass

print(M.mro())