# HTML 사용법

````python
# sort import 하면 외장순서-다운로드 순, 알파벳순으로 정렬된다
import datetime

from art import *  #import * == 모든 함수 다 꺼내기
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)
# result=result를 a=b 형태로 볼 때, a는 html에서 출력될 값이고 b는 python에서 코딩된 값이다. b를 a에 저장한 것이지, 같다는 것이 아니다.


@app.route('/') #'/'는 가장 첫 페이지
def index():
    return render_template('index.html')


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    enddate = datetime.datetime(2019, 11, 29)
    left = enddate - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '알라딘',
        '스파이더맨 파 프롬 홈',
        '토이스토리4',
        '라이온 킹',
        '기생충'
    ]
    return render_template('boxoffice.html', movies=top_5)


@app.route('/send')
def send():
    return render_template('send.html')


#method의 기본 값은 GET이며, 이는 url에 사용자의 입력값이 모두 보인다. POST를 method로 사용해야 private하고 정보를 전송할 수 있다.
@app.route('/receive', methods=['POST']) 
def receive():
    data = request.form.get('msg')
    stock = Stock(data, token='pk_63c229409ff14b67a6cc81e38927f1c4').get_quote()
    company_name = stock['companyName']
    latest_price = stock['iexRealtimePrice']
    return render_template("receive.html", c_name=company_name, l_price=latest_price)

if __name__ == '__main__':
    app.run(debug=True)

````

index.html

````html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Index</title>
</head>
<body>
    <nav> #nav==navigation
        <ul>
            <li><a href="/dday">dday</a></li> #<a href=url>은 하이퍼링크 생성
            <li><a href="/boxoffice">boxoffice</a></li>
            <li><a href="#">dunno</a></li>
        </ul>
    </nav>    
</body>
</html>
````

dday.html

````html
<!DOCTYPE html>
<html lang="ko"> #html 문서에서 가장 많이 쓰는 언어가 한국어이다.
<head>
    <meta charset="UTF-8">
    <title>D-day</title>
</head>
<body>
    <h1>SSAFY 2기 1학기 종료까지</h1>
    <h2>{{ left_days }}일 남았습니다</h2> #{{ 내용 }}은 flask에서 받아서 출력되는 것 
</body>
</html>
````

boxoffice.html

`````html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Box office</title>
</head>
<body>
    <h1>box office</h1>
    <ol>
        {% for movie in movies:  %}   #python 문법을 {% %}을 사용하면 html에서도 실행할 수 있다
            <li>{{ movie }}</li>
        {% endfor %}				  #혹시 모르니까 종료 조건을 확실히 해준다
    </ol>
</body>
</html>
`````

art.html

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>make art</title>
</head>
<body>
    <h1>Put some text</h1>
    <form action="/result"> 
        <input type="text" name="input_text"> #input은 closing이 필요 없다
        <select name="font"> #select은 사용자에게 선택값을 제시해주는 것
            #key와 value는 다르다. key는 사용자가 보는 것. value가 진짜로 전송되는 값.
            <option value="random">랜덤</option>  
            <option value="block">블록</option>
            <option value="white_bubble">원</option>
        </select>
        <input type="submit" value="submit"> 
    </form>
</body>
</html>
````

result.html

`````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>result</title>
</head>
<body>
    <h1>Result</h1>
    <pre>
        {{ result }}
    </pre>
</body>
</html>
`````

send.html

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>send message</title>
</head>
<body>
    <h1>send message here</h1>
    <form action="/receive" method="POST"> #action은 받는 서버의 주소이다
        <input type="text" name="msg"> #name을 지정해야 서버에서 받을 수 있음
        <input type="submit" value="보내기">
    </form>
</body>
</html>
````

receive.html

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Receive</title>
</head>
<body>
    <h1>{{ c_name }}</h1>
    <h1>${{ l_price }}</h1>
</body>
</html>
````



상세의 정도 id>class>name

selector(선택자) 개념을 위해 id, class를 사용

id=문서 내 단 한개만 존재 가능

class= 문서 내 여러개 존재

name= 서버에서 문서를 받아볼려고 쓰는 것

flask 문법 `{{ }}`은 굳이 기억하지 말자