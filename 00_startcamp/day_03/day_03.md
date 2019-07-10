# 함수 quiz

​	`input()`: () 값에 사용자가 입력한 값을 받는다

````python
name = input()
print('hi' + name)

````

````python
#input('요구사항')으로 하면 요구사항을 먼저 출력해서 보여준다
name = input('what is your name?')
print('hi' + name)

````

````python
# ' 앞에 \을 써주면 문자로 인식된다
name = input('what\'s your name?: ')
print('hi' + name)

````

````python
# words의 첫 글자와 마지막 글자를 출력하라
words = input('입력 고고: ')
print(words[0], words[-1])
#words의 class type은 str(string)
#'list name'[-1]은 'list name[list's length-1]'을 의미한다. 그래서 늘 마지막 list 값을 의미한다

import random

length = random.choice(range(1, 100))
unknown = list(range(length))

print(unknown[length-1])
print([unknown-1])

````



string(str)은 문자열을 뜻한다

컴퓨터의 물리 세계에서는 한 칸에 하나만 저장한다. 즉, string도 list와 같이 문자 하나하나의 집합이라는 것이다.

그래서 words를 list화 하지 않아도 바로 list와 같은 함수 기호를 써서 출력 가능했던 것이다.



range (시작숫자, 종료숫자, step)

시작 숫자와 step은 생략하면 시작숫자==0, step==1로 설정된다.

숫자는 00번째를 의미한다고 생각하면 편하다.

컴퓨터는 0부터 세기 때문에 0번째는 0, 1번째는 1, 5번째는 4, 100번째는 99 이런식으로 받아들인다.

ex) `range(1,5,1)`==[1,2,3,4]

````python
# 자연수 n을 입력받고, 1 부터 n까지 출력하라

numbers = input('자연수를 입력하라: ')
numbers = int(numbers)
#int()은 class type을 interger로 바꾸는 함수
#''을 없앴을 때 int로 바꿀 수 있는 것은 10진수의 수이다.

n = list(range(1, numbers+1))
for numbers in n:
    print(numbers)
    numbers+=1
print(type(numbers)) >> interger

print(n)
print(type(n)) >> list

for i in range(numbers-1):
    print(i+1, end=',')
print(type(i)) >> interger

````

````python
#짝수, 홀수를 구분하자
number = int(input('숫자를 입력하세요: '))

if number % 2 == 0:
    print('짝수')
else:
    print('홀수')
    
# %는 나누기 후 나머지를 의미한다
````



git bash의 $는 'im listening', 즉 명령어를 받을 준비가 되어있다는 뜻

ctrl+c == terminal 내 cancel

ctrl+d == terminal 종료

작업 단위 하나하나를 process라고 한다

````python
# fizz buzz > 3의 배수에서 fizz 출력, 5배수에서 buzz, 15배수에서 fizzbuzz

numbers = int(input('숫자를 입력하세요: '))
for n in range(1, numbers+1):
    if n % 15 == 0:
        print('fizzbuzz')
    elif n % 5 == 0:
        print('buzz')
    elif n % 3 == 0:
        print('fizz')
    else:
        print(n)

````

# Web API

web scraping: 사람이 직접 web에서 정보를 긁어오는 것. 제일 귀찮다.

web API: API를 통해서 정보를 긁어오는 것

````python
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
data = json.loads(response)

print(data['bnusNo'])

real_numbers = []
for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)

````

JSON은 JavaScript Object Notation의 줄임말로, 기본적으로 키-값쌍의 포맷으로 구조화된 정보를 인코딩하는 규격이다. JSON은 이러한 호환 타입 객체를 인코딩한 바이트(bytes) 객체이며, 파이썬의 사전처럼 조작하거나 특정 키를 통해서 액세스할 수 없는 상태가 된다. JSON 호환 타입 객체를 JSON 데이터로 인코딩하는 함수가 `dump()` 이고, `load()`는 이런 데이터를 Python 객체로 환원한다. 각각의 함수에 `s` 가 붙은 버전은 “문자열 기반”으로 말 그대로 JSON을 표현하는 문자열로 변환하거나, 그 반대의 변환을 가리킨다. 즉, `dumps()`는 사전 객체를 JSON 문자열로 변환하고, `loads()`는 그 반대를 수행한다.

`f'letters{n}'`: f는 format을 의미한다. {} 자리에 n을 쓴다.

# Web Module/ Package

````python
from iexfinance.stocks import Stock

company = Stock('TSLA', token='pk_numbers')

print(company.get_price())

company = Stock('AAPL', token='pk_numbers')

print(company.get_quote())
````



# Flask

````python
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto_


@app.route('/hello/<name>')  # var routing
def hello(name):
    return f'hi,{name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '마라탕',
        '마라샹궈',
        '탕수육',
        '양장피'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:number>')
def cube(number):
    return str(number ** 3)


if __name__ == '__main__':
    app.run(debug=True)

````



# HTML

````html
<!DOCTYPE html>
<html>
    <head>   
<!-- head에 쓰는 것은 보이지 않는다. head = 정보 -->
        <meta charset="utf-8">
    </head>
    <body>
<!-- body에 쓰는 것은 보인다. body = 내용 -->
        Hyper
        Text
        Markup
        Language
        <h1>Today I Learned</h1>
        <h2>Learn Flask</h2>
        <ol>
            <li>pip install flask</li>
            <li>touch app.py</li>
            <li>python app.py</li>
        </ol> 
        <h2>Learn HTML</h2>
        <ul> 
            <li>doctype html</li>
            <li>head, body</li>
            <li>h1, h2, ol(number list), ul(shape list), li(line)</li>
        </ul>    
    </body>
</html>
````

