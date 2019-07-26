def add(a, b):
    return a + b


def sub(a,b):
    return abs(a-b)

    
def mul(a,b):
    return a * b


def div(a,b):
    try:
        return a / b
    except ZeroDivisionError as err:
        return '0으로 나눌 수 없습니다.'


print(div(1,2))
print(div(1,0))
# 이 두개의 print가 정확하게 이 파일을 실행했을 때만, 실행되면 좋겠다. ($ python calc.py)
# 지금은 import calc 하면 이 두개의 값이 같이 나온다.
# print(__name__) => '__main__'
# __name__은 이 파일이 main 실행 파일이라는 것을 나타내는 변수로, __name__이 있는 파일만 __main__으로 되고 그 외는 파일 이름이 나온다.
# if __name__ = __main__ 이라는 조건을 붙여주고 쓰면, print(div(1,2)), print(div(1,0))가 calc이 실행될 때만 출력한다.


