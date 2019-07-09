# 190708 startcamp-day1

## 컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터는 계산기이다

### 프로그래밍

명령어의 집합

일을 쉽게 시키는 것

### 언어

약속

## Python 기초 문법 3형식

1. 저장

   =는 저장하다. ==는 같다.

   `dust=60` ~ dust라는 박스에 60을 저장하다

   list []

   `dust=[20,34]`

   dictionary {}

   `dust={'강남구청': 80, '영등포구': 40}`

   출력은 꼭 []로 한다.

   `print(dust['강남구청'])` / `print (dust[0])`

   출력 : 80/ 20

   #컴퓨터는 0부터 숫자를 센다는 것을 기억할 것

   #박스는 마지막으로 저장한 것이 출력된다

   #박스에서 출력하고 싶은 것을 고려해서 비우고, 저장하는 일을 할 것

2. 조건

   true/false

   if~: 만약 ~라면

   elif~: if에서 해당 안되는 것 중 이 if에는 해당된다면~

   else~: 위의 if에 해당 안된다면~

   #조건문 뒤에는 : 을 붙여야 실행이 된다

   #앞 쪽 if문을 지나온 것은 이미 그 조건에 해당되지 않아 넘어온 것이라는 것을 기억해서 간단하게 코드를 짤 수 있도록 하기

3. 반복: 

   while ~: 계속 실행 + 종료 조건 필요

   for ~: 반복문 + 종료 조건 불필요 ex)`for i in numbers` 

## Python 함수

python 함수에는 내장 함수와 외장 함수가 있다.

- 내장함수

  - `print()`: 출력하는 함수

  - `range()`: 범위를 생성하는 함수

    #컴퓨터는 0부터 세기에 `range(1,46)` 이라고 하면 1부터 45가 나온다.

  - `list()`: 리스트를 생성하는 함수

- 외장 함수

  - `random`: 랜덤 관련 함수들의 묶음
  - `random.choice(p)`: 리스트에서 1개 무작위 선택
  - `random.sample(p,k)`: 모집단p 에서 k 개의 요소를 무작위 비복원 선택

### 로또 번호 추첨 하기

```python
import random
numbers=list(range(1,46))
lucky_numbers=random.sample(numbers,6)
print(lucky_numbers)

import random
lucky_numbers=random.sample(range(1,46),6)
print(lucky_numbers)

#range는 범위 함수이기에 사실 소수점 숫자들도 전부 포함되어있다. 단지, list라는 함수에는 정수라는 약속이 포함되어있고, list가 없을 때는 컴퓨터가 임의로 정수만 배출한 것이다. 소수가 나올 수도 있다.
```

## API

API(Application Programming Interface): 시스템 간의 연결

