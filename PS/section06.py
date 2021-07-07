# multiple return function
# *args, *kwargs

def args_function(*args):   # 매개변수 갯수가 몇개인지 상관 없이 다 튜플로 반환
    for i, v in enumerate(args):
        print(i, v) # 인덱스를 만들어줌.

args_function('kim')

# kwargs
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1='kem', name2="oarj")

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20, 'park', 'kim', age1=24, age2=24)

# 중첩함수(클로저) 변수의 선언을 줄일 수 있음, 메모리 관리 효율적으로 할 수 있음
# 데코레이터

def nested_func(num):
    def func_in_func(num):
        print(num)
    print('in func')
    func_in_func(num + 10000)

nested_func(10000)

# hint : 형을 알려줌. 근데 예외처리는 못함(?)]

def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]
print(func_mul3(5))

# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10

lambda_mul_10 = lambda num: num * 10
