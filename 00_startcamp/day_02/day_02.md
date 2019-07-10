# What is Git? 

git: scm (source code manager) / vcs (version control system)

버전 관리를 해주는 cctv

## 명령어

`git init`: 이 dic에 git을 넣음 - master가 붙음

`cd dic명`: dic으로 들어가기

`cd ..`: 위의 dic으로 가기

`touch file명`: fiie 생성

`mkdir dic명`: dic 생성

`rm dic명`: dic 삭제

`git status`: dic 안의 상태 명시

`ls`: list. 내 상태에서 무엇이 있는가 리스트로 보여줘.

`git add <filename>`: git 이 file 감시해줘

`git commit -m 'message'` : 이 메세지로 저장해줘

`git add <filename>`: git이 사진 찍을 수 있도록 멈춰 (변경사항 저장 후 다시 재저장하기 전)

`git log`:  사진(commit/ 저장사항)들의 로그를 보여줌 (최신부터 역순으로 보여줌)

`git push`: git에 백업하기

`git remote add <drive name>`:  내 백업은 여기로 보내

`git remote -v`: 내 백업 공간은 어디야?

`git push <drive name> master`:  <drive name>으로 백업 해줘

`git add -A`: 여러개를 한 번에 저장할게

`git add . ` : 여러 개를 한 번에 저장할게

`touch .gitignore`: gitignore라는 git에서 숨겨진 dic을 만든다

#점(.)이 붙으면 숨기는 폴더/파일이라는 뜻

#tab 누르면 파일명을 쉽게 쓸 수 있음

## 내 git sign

````git
git config-global user.email "email"

git config-global user.name "name"
````

# Web

## Web browser 열기

```python
import webbrowser
urls=[
	'www.naver.com',
    'www.google.com',
    'www.slack.com',
    'www.github.com',
    'www.youtube.com'
]

for url in urls:
     webbrowser.open(url)

or
        
i=0
while i < 5:
webbrowser.open(urls[i])
i += 1
```


# Web에서의 커뮤니케이션 방식

요청(주소)과 응답(문서) : 주소로 요청을 보내고 문서를 응답으로 받는다

`pip install <함수명>`: 내 책상 위에도, 서랍 안에도 없는 함수를 다운로드 한다 ex) `pip install requests`

`requests.get('url')`: web 요청 함수

````python
import requests

response = requests.get('https://naver.com').text
print(response)

#text가 없으면 response [200]이 나온다. response [200] == okay.
#text가 있으면 페이지 소스가 전체 다 출력된다
````

bs4(BeautifulSoup) = python이 읽기 힘든 페이지 소스를 읽기 쉽게 해주는 함수

`text = bs4.BeautifulSoup(변수)` : 출력될 변수인 페이지 소스를 bs에 한 번 넣어주는 것

````python
import requests
import bs4

#url 정의
url = 'https://finance.naver.com/sise/'

#변수 response에 url에 request한 text를 저장한다
response = requests.get(url).text

#변수 text에 beautiful soup에 넣었다 뺀 변수 response의 값을 저장한다
#'html.parser'는 beautiful soup에서 뺄 때 어떤 형태로 나올 지 정하는 것
text = bs4.BeautifulSoup(response, 'html.parser')

#변수 kospi에 변수 text의 값 중 KOSPI_now라는 값을 "하나" 선택해서 저장한다
kospi = text.select_one('#KOSPI_now') 

#변수 kospi의 값 중 text 형태인 값을 출력한다
print(kospi.text)

#KOSPI_now = <span class="num num2" id="KOSPI_now">2,052.03</span>
#KOSPI_now는 페이지 소스에서 원하는 것을 copy selector 해서 가져온 것
#함수는 ()을 포함한다
````



````python
import requests
import bs4

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(exchange_rate.text)

````



````python
import bs4
import requests

url = 'https://www.melon.com/chart/index.htm'

#모든 요청에 응답해주지 않는다. 이 때, 어떤 browser가 보냈는지 인 user agent를 다시 설정해준다.
headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')

#변수 rows에 변수 text의 값 중 .lst50라는 값을 "모두" 선택해서 저장한다.
rows = text.select('.lst50')

#멜론에서 받은 .lst50에서 원하는 정보를 선택해서 뽑을 수 있다.
for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    
    #여러 개의 값을 출력할 수 있다.
    print(rank, title, artist)

````

# File control

## CSV (Comma Seperate Value)

1, 벤, 헤어져서 고마워

2, 청하, snapping

...

콤마로 구별하는 값들

코드로 csv를 쓰면 여러 값들을 정리해서 문서로 쓰고, 엑셀로 불러올 수도 있다.

`with open ()`: ()을 여는 함수

`with open ('file name', 'w/r')`: 파일을 쓰는 버전 또는 읽는 버전으로 실행

`f.write/read`: file을 써라/ 읽어라

````python
lunches = {
    '양자강': '02-888-9999',
    '김밥카페': '02-578-9654',
    '순남시래기': '02-634-9871'
}

#lunch.csv라는 파일을 utf-8(한글)로 엔코딩해서 write 하고 f로 저장해서 open 해라
with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    #lunches.items에서 name, phone을 반복해서
    for name, phone in lunches.items():
        f.write(f'{name},{phone}\n') 
        #\n은 줄바꿈 역할을 한다

#dictionary에서 key와 value를 모두 출력한다
for key,value in lunches.items():
   print(key,value)

````

````python
import csv

#lunch.csv라는 파일을 utf-8(한글)로 엔코딩해서 read 하고 f로 저장해서 open 해라
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)

````

`writer.writerow([0,1,2])`:  writer.writerow에는 enter 치는 것이 포함되어있다.

`````python
import bs4
import requests
import csv

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = text.select('.lst50')

#writer로 csv.writer를 고용하여 open 함수대로 쓰게 한다
writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline=''))
#표 제일 위에서 분류하는 값의 이름을 list 대로 정한다
writer.writerow(['순위', '제목', '가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    #writer가 한 줄씩 enter를 포함해서 써준다 (그래서 newline 함수를 썼음)
    writer.writerow([rank, title, artist])

`````



