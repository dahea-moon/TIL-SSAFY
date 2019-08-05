# 프로그래밍 언어 과목평가 노트정리

## 1. Python 기초: 

### 1.1 식별자

식별자: 변수, 함수, 모듈, 클래스 등을 식별하는 데 사용되는 이름

convention: 

* 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.

* 첫 글자에 숫자가 올 수 없다.

* 대소문자를 구별한다.

* 예약어는 사용할 수 없다.

  ```python
  False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

* 내장함수나 모듈 등의 이름으로도 만들면 안된다.
* 예약어, 내장함수, 모듈 등의 이름으로 변수를 만들면 기존의 기능이 덮어쓰여지므로 식별자 이름으로 쓰면 안된다.

### 1.2 기초 문법

인코딩 선언: default로 UTF-8이 설정되어 있다. 인코딩 선언은 Python `parser`에 의하여 읽혀지며, `# -*-coding:<encoding-name>-*-`이라 선언한다.

주석: `#`으로 표현하는 것이 기본이다. 여러 줄의 주석을 작성할 때에는, `"""`으로 `docstring` 을 표현하면 된다.

코드라인: 기본적으로 파이썬에서는 `;`을 작성하지 않는다. 그러나 한 줄로 표기할 때에는 `;`으로 작성한다. `\`으로도 가능하다. list, set, dict은 특별한 표기 없이 한 줄 작성이 가능하다.

```python
print('Happy'); print('Hacking')
print('Happy\
Hacking')
```

### 1.3 변수 및 자료형

* 변수는 `=`을 통해 할당(assignment) 된다.

* `type()`을 통해 자료형을 확인해야한다.

* 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

* 같은 값을 동시에 할당 할 수 있다.

  ```python
  a = b = 10
  ```

* 다른 값을 동시에 할당 가능하다.

  ```python
  a, b = 1, 2
  ```

* 변수의 갯수가 값의 갯수보다 더 적거나 많으면 오류가 발생한다.

* ```python
  # 변수의 값 바꾸기
  a = 10
  b = 20
  
  # 1. tmp var 사용
  c = a
  a = b
  b = c
  
  # 2. +, - 사용
  a = a + b
  b = a - b
  a = a - b
  ```

### 1.4 수치형(Numbers)

#### (1) `int`: 정수

* 모든 정수는 `int`로 표현된다.
* 8진수: `0o`, 2진수: `0b`, 16진수: `0x`
* Overflow (일반적) vs Arbitrary-precision arithmetic (Python)
  - 일반적으로, 데이터 타입 별로 사용할 수 있는 메모리 크기가 제한되어 있다. 표현할 수 있는 수의 범위가 넘어가면 메모리의 넘친(overflow) 현상으로 이상한 값이 출력된다.
  - 파이썬은 아주 큰 정수를 표현할 때, 메모리의 변화한다. 가용 메모리를 모두 수 표현에 끌어다 쓸 수 있어 유동적인 운용이 가능하다.

#### (2) `float`: 부동소수점, 실수

* 실수는 부동소수점으로 표현되며, 항상 같은 값으로 일치되지 않는다.

* 숫자를 표현하는 과정에서 생기는 오류는 대부분 중요하지 않으나, 값 비교 과정에서는 문제가 발생할 수 있다.

* 실수의 경우, 덧셈은 괜찮으나 뺄셈 처리 시에는 오류가 있을 수 있다.

* `round()` 를 통해 반올림하여 실수를 정리 할 수 있다.

* 실수 비교 방법

  ```python
  # 1. abs
  if abs(a-b) <= 1e-10:
  	print('대충 같다')
  	
  # 2. sys module
  if abs(a - b) <= sys.float_info.epsilon:
  	print('대충 같다')
  
  # 3. math module
  import math
  
  math.isclose(a, b)
  # output: True
  ```

#### (3) `complex`  : 복소수

* 복소수는 허수부를 `j`로 표현한다.

  ```python
  a = 3 + 4j
  
  a.imag => 허수부 출력
  a.real => 실수부 출력
  a.conjugate() => 
  ```

  

### 1.5 Bool

* `True`와 `False`로 이뤄진 `bool` 타입

* `bool(value)` 하면 `True`와 `False` 가 출력된다.

* `False`의 경우: [], 0, {}, 0.0, '', (), None

* `True`의 경우: `False` 경우 제외 전부.  어떤 값이나 type 이든 비어있지 않고 무언가가 존재 하면 `True`이다. 예로, `[False]`, `[0]`, `' '` 등 도 전부 `True`이다.

  

### 1.6 None

* 값이 없음을 표현하는 `None` 타입이 존재한다.

  

### 1.7 String: 문자형

* 문자열은 `''` 나 `""`을 활용하여 표현 가능하다.

* 하나의 문자열을 묶을 때 동일한 문장부호를 활용해야 한다.

* `PEP-8`에서는 하나의 문장부호를 선택하여 유지하는 것이 원칙이다.

* 사용자에게 받은 입력은 기본적으로 `str` 이다.

* 여러 줄에 걸쳐있는 문장은 `""" """`  을 사용 하여 표현 합니다.

* 이스케이프 문자열

  * 특수문자 또는 조작을 하기 위하여  `\` 을 활용하는 문자열

  * | 예약문자 |   내용(의미)    |
    | :------: | :-------------: |
    |    \n    |     줄바꿈      |
    |    \t    |       탭        |
    |    \r    |   캐리지리턴    |
    |    \0    |    널(Null)     |
    |   `\\`   |       `\`       |
    |    '     | 단일인용부호(') |
    |    "     | 이중인용부호(") |

  * 문자열 뒤에 `end='escape string'`을 쓰면 출력 결과를 조정할 수 있다.
  
* String Interpolation

  ```python
  name = '김싸피'
  ```

  * %-formatting

    `'Hello, %s' % name`

  * str.format()

    `'Hello, {} {} {}'.format(name, 100, True) #순서대로 들어간다`

  * f-strings

    `f'Hello, {name}'`

### 1.8 연산자

* 산술 연산자

  | 연산자 |      내용      |
  | :----: | :------------: |
  |   +    |      덧셈      |
  |   -    |      뺄셈      |
  |   *    |      곱셈      |
  |   /    |     나눗셈     |
  |   //   |       몫       |
  |   %    | 나머지(modulo) |
  |   **   |     거듭제     |

* 비교 연산자

  | 연산자 |  내용  |
  | :----: | :----: |
  | a > b  |  초과  |
  | a < b  |  미만  |
  | a >= b |  이상  |
  | a <= b |  이하  |
  | a == b |  같음  |
  | a != b | 같지않 |

* 논리 연산자

  | 연산자  |            내용             |
  | :-----: | :-------------------------: |
  | a and b |  a와 b 모두 True시만 True   |
  | a or b  | a 와 b 모두 False시만 False |
  |  not a  | True -> False, False -> Tru |

  * 참거짓 판단에서는 판단을 위해 고려하는 가장 마지막 값을 출력한다.

* 복합 연산자

  * 연산과 대입이 함께 이뤄진다.

    |  연산자   |    내용    |
    | :-------: | :--------: |
    |  a += b   | a = a + b  |
    |  a -= b   | a = a - b  |
    |  a \*= b  | a = a \* b |
    |  a /= b   | a = a / b  |
    |  a //= b  | a = a // b |
    |  a %= b   | a = a % b  |
    | a \*\*= b | a = a ** b |

* Concatenation: 자료형을 합치는 `+` 연산자
* Containment Test: `in` 연산자를 통해 속해있는지 여부를 확인
* Identity: `is` 연산자를 통해 동일한 object인지 확인
* 연산자 우선순위
  0. `()`을 통한 grouping
  1. Slicing  ` [ : ] `
  2. Indexing  `[0]`
  3. 제곱연산자: `**`
  4. 단항연산자: `+`, `-` (음수/양수 부호)
  5. 산술연산자: `\*`, `/`, `%`, `//`
  6. 산술연산자: `+`, `-`
  7. 비교연산자, `in`, `is`
  8. `not`
  9. `and` 
  10. `or`

### 1.9 기초 형 변환(Type Conversion)

* 암시적 형변환
  * 사용자가 의도하지 않았지만, 파이썬 내부에서 자동으로 형변환 하는 경우: `bool`, `numbers(int, float, complex)`
  * `bool`은 `true`는 1로, `false`는 0으로 자동 변환
  * Numbers는 연산 시 1) `complex`, 2) `float`, 3) `int` 우선순위 순으로 변환된다.
* 명시적 형변환
  * 암시적 형변환을 제외하고는 모두 명시적으로 형 변환
  * `int()`: string, float을 int로 변환
  * `float()`: string, int 를 float으로 변환
  * `str()`: int, float, list, tuple, dictionary를 문자열로 변환
  * `string` -> `intger` : 형식에 맞는 숫자만 가능
  * `integer` -> `string` : 모두 가능
  * 2가지 형 변환을 한 번에 할 수 없음. ex) `int('3.5')`
  * `float`을 `int`로 형변환하면 내림 숫자가 나옴

### 1.10 시퀀스(sequence) 자료형

* 시퀀스(sequence): 데이터의 순서대로 나열된 형식
* 정렬되었다라는 뜻은 아니다
* list, tuple, range, string, binary

(1) list (리스트): `[value1, value2, value3]`

- 리스트는 대괄호 `[]`로 만들 수 있다
- 값에 대한 접근: `list[i]`

(2) tuple(튜플): `(value1, value2)`

- 리스트와 유사, `()`로 묶어서 표현

- 수정불가능(immutable)하고, 읽을 수 밖에 없음

- 직접 사용 보다는 파이썬 내부에서 사용

  ````python
  # tuple을 만들어봅시다.
  tup = (1, 2)
  print(tup, type(tup))
  
  # 아래와 같이 만들 수 있습니다.
  x = 1, 2
  print(x, type(x))
  
  # 파이썬 내부에서는 다음과 같이 활용됩니다.
  # 앞선 2. 변수 및 자료형 예제에서 사용된 코드입니다.
  x, y = 1, 2
  # 실제로는 x, y = (1, 2) 형태로, tuple 처리 됩니다.
  
  # 변수의 값을 swap하는 코드 역시 tuple을 활용하고 있습니다. 
  x, y = y, x
  
  tup = 1, 2, 3, 4, 5, 'a', 'b'
  print(tup, type(tup))
  
  tup[5]
  output: (1, 2, 3, 4, 5, 'a', 'b')<class 'tuple'>
  		'a'
  ````

(3) range: 숫자의 시퀀스

- `range(n)`: 0<= x < n
- `range(n, m)` : n <= x < m
- `range(n, m, s)`: n <= x < m (스텝: s)
- range의 기본형은 tuple

(4) 시퀀스 연산자/ 함수

| operation  | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| x in s     | containment test (bool)                                      |
| x not in s | containment test (bool)                                      |
| s1 + s2    | concatenation (이어붙이기; numbers 제외)                     |
| s * n      | n번만큼 반복하여 더하기(numbers 제외)                        |
| s[i]       | indexing                                                     |
| s[i:j]     | slicing ( i <= index < j)                                    |
| s[i:j:k]   | k간격으로 slicing (i <= j <, 간격: k) ; 빈칸으로 두면 마지막 value까지를 의미, 간격을 -1로 두면 거꾸로 step을 가는 것 |
| len(s)     | 길이                                                         |
| min(s)     | 최솟값                                                       |
| max(s)     | 최댓값                                                       |
| s.count(x) | x의 갯수                                                     |

### 1.11 non-sequence type

- `set`과 `dictionary`는 기본적으로 순서가 없다

(1) `set`: {value 1, value 2, value 3}

- 수학의 집합과 동일하게 처리

- 순서가 없고, 중복된 값이 없다

- set을 활용하면 list의 중복된 값을 손쉽게 제거할 수 있다

- 활용법

  | 연산자/함수       | 설명   |
  | ----------------- | ------ |
  | a - b             | 차집합 |
  | a \| b            | 합집합 |
  | a & b             | 교집합 |
  | a.difference(b)   | 차집합 |
  | a.union(b)        | 합집합 |
  | a.intersection(b) | 교집합 |

(2) `dictionary`: {key1: value1, key2: value2, key3: value3, ...}

- `key`와 `value`가 쌍으로 이루어져있다
- literal `{}` 과 생성자 함수 `dict()`로 만들 수 있다.
- `key`는 immutable한 모든 것이 가능 (string, integer, float, boolean, tuple, range)
- `value`는 list, dictionary를 포함한 모든 것이 가능하다.
- 중복된 `key`는 존재 할 수가 없다.



### 총정리

데이터 타입

container:

(1) sequence (ordered)

​	string, list, tuple, range

(2) unordered

​	set, dictionary

changeable?:

(1) immutable

​	string, tuple, range, bool, numbers ( int, float, complex )

(2) mutable

​	list, set, dictionary



## 2. 제어문 (Control of Flow)

### 2.1 조건문 (if문)

- `if <조건식>` : 반드시 일정한 참/거짓을 판단할 수 있는 조건식과 사용
  - 조건식이 참인 경우:  `:`  이후의 문장을 수행
  - 조건식이 거짓인 경우: `else:` 이후의 문장을 수행

- 복수 조건문: 2개 이상의 조건문을 활용할 경우 `elif <조건문>: ` 을 활용
- 중첩 조건문: `if`  안에 `if` 실행
- 조건 표현식(conditional expression):
  - `true_value if <조건식> else false_value`

### 2.2 반복문

#### (1) while 문: `while True:`

`while` 문은 조건식이 `True` 인 경우 반복적으로 코드를 실행

종료조건을 반드시 설정해줘야 한다.

### (2) `for`문: `for value in sequence:`

정해진 범위 내 (시퀀스) 에서 순차적으로 코드를 실행

범위가 이미 정해져 있기 때문에, 종료조건을 설정해주지 않아도 된다.

** `iterable` 이라는 것은 시퀀스, 이터레이터 또는 이터레이션을 지원하는 객체, 즉 열거 객체

- index와 `for`문
  - `enumerate(iterable)`: index와 value를 반환하는 함수
  - `for index, value in enumerate(iterable)`
- dictionary 반복문
  - `for key in dict:` key 반환 및 반복
  - `for key in dict.keys()`: key 반환 및 반복
  - `for value in dict.values()`: value 반환 및 반복
  - `for key, value in dict.items()` : key와 value 반환 및 반복

### (3) `break`, `continue`, `else`

- `break` : 반복문을 종료하는 표현
- `continue` : continue 이후의 코드를 수행하지 않고 다음 요소를 선택해 반복을 계속 수행
- `else` : 끝까지 반복문을 시행한 이후에 실행. `break`를 통해 중간에 종료되지 않은 경우에만 실행. `for~else`를 의미한다.



## 3.  function (함수)

### 3.1 함수 정의

```python
def func(parameter1, parameter2):
	code line1
	code line2
	return value
```

- parameter == 매개변수
- return을 통해 결과값을 전달
- return 값이 없으면, None을 반환
- 호출은 `func(val1, val2)`로 한다
- return은 모든 종류의 객체를 반환할 수 있다. 단, 오직 한 개의 객체만 반환된다.
- 단 하나의 객체만 반환되지만, 값은 여러개 반환될 수 있고 이럴 때에는 하나의 tuple로 묶여서 반환된다.

### 3.2 인수(parameter)

(1) 위치 인수

- 함수는 기본적으로 인수를 위치로 판단

- 기본값(Default Value): 

  - 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있다.
  - 기본 값이 있는 ''매개변수'' 뒤에 기본 값이 없는 ''매개변수''를 사용 할 수는 없다.

  ```python
  def greeting(age, name= 'john'):
  	print(name, age)
  ```

(2) 키워드 인자

- 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있다.

- 키워드 인자 뒤에 위치 인자를 사용 할 수는 없다.

- 위치 ''인자'' => 키워드 ''인자'' 순서 이어야 한다.

  ```python
  greeting('neo', age=10)
  ```

(3) 가변 인자

- 정해지지 않은 임의의 개수의 인자를 받기 위한 가변인자
- tuple 형태로 처리
- `def func(*args)`

(4) 정의되지 않은 키워드 인자

- dict 형태로 처리
- `def func(**kwargs)`

(5) 딕셔너리를 인자로 넘기기

- `**dict` 를 통해 함수에 딕셔너리를 인자로 넘길 수 있다
- `func(**dict)`

### 3.3 이름공간 및 스코프(Scope)

- 파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있다.

- 인식 우선순위 (LEGB Rule)

  (1) Local scope: 정의된 함수

  (2) Enclosed scope: 상위 함수

  (3) Global scope: 함수 밖의 변수 혹은 import된 모듈

  (4) Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

- 수명주기 순위

  (1) Built-in scope: 파이썬이 실행된 이후부터 끝까지

  (2) Global scope: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지

  (3) Local/Enclosed scope: 함수가 실행된 시점 이후부터 리턴할때까지

### 3.4 재귀함수(recursive function)

- 재귀함수: 함수 내부에서 자기 자신을 호출하는 함수

- 재귀함수는 기본적으로 같은 문제이지만, 점점 범위가 줄어드는 문제를 풀게 된다

- 재귀 함수 작성시에는 반드시, base case가 있어야 한다.

- base case는 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳이다.

- 재귀 함수의 장/단점

  - 알고리즘 구현에 적절 (더 자연스럽다)
  - '변수 사용'을 줄여준다
  - 코드가 더 직관적이고 이해하기 쉬운 경우가 있다
  - 만들기는 어렵다
  - 함수가 호출될 때 마다 메모리 공간에 쌓인다. 그래서 메모리 스택이 넘치거나 (stack overflow) 프로그램 실행속도가 느려진다.
  - 파이썬에서는 이를 방지하기 위해 1,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다.

  ```python
  # 팩토리얼
  def factorial(n):
      if n == 1:
          return 1  # n
      else:
          return n * factorial(n-1)  
      
  factorial(4)
  
  # 피보나치 수열
  def fib(n):
      if n == 0 or n == 1:
          return 1
      else:
          return fib(n-1) + fib(n-2)
  
  fib(4)
  ```



## 4. Data structure (자료구조)

### 4.1 String method (문자열 메소드)

(1) `.capitalize()` : 앞글자를 대문자로 만들어 반환합니다. + 나머지는 모두 소문자. ex) `string.capitalize()`

(2) `.title()` : 어포스트로피나 공백 뒤에 있는 문자를 대문자로 만들어 반환. ex) `string.title()`

(3) `.upper()` : 모두 대문자로 만들어 반환. ex)`string.upper()`

(4)`.lower()` : 모두 소문자로 만들어 반환. ex) `string.lower()`

(5)`.swapcase()`: 대 <-> 소문자로 변경하여 반환

(6) `'arg'.join(iterable)` : iterable type의 객체를 특정한 문자열로 만들어 반환

arg을 넣는 기준은 string은 각 value 뒤, 그 외 iterable은  ',' 이다.	

```python
'!'.join('배고파') -> output: 배!고!파!

'-'.join(['hi', 'hello']) -> output: hi-hello
```

(7) `<class str>. replace(old, new[, count])` : 바꿀 대상의 글자를 새로운 글자로 바꿔서 반환. count를 지정하면 해당 갯수만큼만 시행.

```python
'yayaya!'.replace('a', '_')
'woooooowooooo'.replace('o', '', 3)
output:
y_y_y_
wooowooooo

s = 'wooooowoooo'
s2 = s.replace('o', 'x')
print(s, s2)
output:
s = wooooowoooo
s2 = wxxxxxwxxxx
```

(8) `.strip([chars])`: 특정한 문자들을 지정하면, 양쪽을 제거한다. 지정하지 않으면 default value는 공백.

(9)`.lstrip([chars])` & `.rstrip([chars])` : 왼쪽제거, 오른쪽 제거

- strip은 패턴을 읽고 제거하기 때문에 chars와 조금이라도 유사한 부분은 제거한다. 예를 들어, 'hehehehihihi'에서 lstrip으로 he를제거하라고 하면 heheheh를 제거해서 ihihi가 나옴.

(10) `.find(x)` : string 내 첫 x의 index를 반환. 없으면, -1를 반환.

(11) `.index(x)` : string 내 첫 x의 index를 반환. 없으면, 오류를 반환.

(12) `.split(chars='arg')` : 문자열을 chars를 기준으로 나누어 리스트로 반환.  chars의 default value는 ' ' (띄어쓰기) 이다.

(13) 그 외 참/거짓 반환 메소드: `.isbulabula()` 

​		ex) `.isdecimal()`, `.isspace()` , `.istitle()`

### 4.2 LIST Method (리스트 메소드)

(1) `.append(x)` :  리스트에 x값을 추가한다. x가 iterable type일 때, iterable value만 뽑아서 추가하는 것이 아니라 하나의 객체로 인식해서 추가한다. 이를 고려해서 사용해야 한다.

ex) `list.append([1, 2])` -> list = `[[1, 2]]`

(2) `.extend(iterable)` : 리스트에 iterable 값을 붙일 수 있다.  iterable 내 value들을 하나씩 리스트에 추가한다. 그래서 string을 넣으면 문자 하나하나씩이 list value로 추가됨으로 주의해야한다.

ex) `list.extend([1, 2])` -> list = `[1, 2]`

(3) `.insert(i, x)` : 정해진 위치 i에 x 값을 추가. i가 list의 길이를 넘어서면 무조건 마지막에 하나만 추가된다.

(4) `.remove(x)` : 리스트에서 값이 x인 것을 삭제. remove는 값이 없으면 오류 발생.

(5) `.pop(i)` : 정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환한다. `i`가  지정되지 않으면 default로 마지막 항목을 삭제하고 반환한다.

(6) `.index(x)` : 원하는 x값을 찾아 index 값을 반환. index 도 찾는 value x가 없으면 오류 발생.

(7) `.count(x)` : list 내 원하는 x 값의 갯수를 반환.

(8) `.sort()` : list를 정렬해줌. `.sorted()`와 다르게 원본 list를 변형시키고, None을 리턴.

(9)`sorted(list)`: iterable을 정렬해서 list로 반환. 원본 list를 변형시키지 않고, 정렬된 list을 리턴.

(10) `.reverse()` :  list 내 value의 순서를 반대로 뒤집는다. (정렬 아님)

(11) 복사

- 파이썬에서 모든 변수는 객체의 주소(id)를 가지고 있을 뿐이다.
  - 변수를 생성하면, 메모리에 객체를 생성하고 변수에는 객체의 주소가 저장된다.
  - namespae에 있는 변수가 memory에 형성된 객체를 가르키고 있다는 뜻이다.
  - mutable 자료형과 immutable 자료형은 서로 다르게 동작한다.
  - 즉, call by reference라는 것.
  - mutable한 자료형인 list, set, dictionary은 namespace에 있는 변수명이 메모리에 있는 자료를 가르키고, 변형 시 원본이 남지 않는다.
  - immutable한 tuple 같은 type은 메모리 내 자료를 가르키지만, 변형 시 원본이 남는다. 

- Shallow Copy
  -  When you make another instance that is referencing the same memory of original instance, it looks like copy instance has copied the original instance. But, actually they reference the same data in memory. So they cannot be said truly copied. 
  - When one of original instance or copied instance has changed, both are changed. It's because data in the memory which both instance have referenced has been changed.
  - `copy_instance = copy.copy(original_instance)`
- Deep Copy
  - When you want to copy an instance for real, you have to use deep copy.
  - `copy_instance = copy.deepcopy(original_instance)`

(12) `.clear()` : 리스트의 모든 항목을 삭제한다.

- literal 하게 list = [] 이라고 한다고 삭제되지 않는다. 이는 value가 삭제되는 것이 아니라, 메모리 내 새로운 빈 list를 지칭하고 있는 것이다.
- clear 메소드를 써야 실제로 value가 삭제된다.
- shallow copy 상황에서, clear를 쓰면 원본과 카피본 모두 삭제 되고, literal 을 사용하면 해당 객체만 빈 리스트를 가르키는 것으로 바뀐다.

(13) List Comprehension

- `list_name = [value to append <조건문/반복문>]`

- 조건문과 반복문이 중첩될 때에는, 상위 명령문을 앞에다 쓰면 된다.

  ex) `even = [number for number in range(1, 10) if number % 2 == 0]`

### 4.3 Dictionary Method (딕셔너리 메소드)

(1) `.pop(key[, default])` : key가 dictionary에 있으면 해당 value를 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 제거하고 반환하다.  default가 없는 상태에서 key가 dictionary에 없으면 KeyError가 발생한다. 

ex) `dict.pop('melon', '없음')` : melon의 값을 반환해주는데, 만약 없다면 default value인 없음을 반환해줘.

(2) `.update(key=value)` : 값을 제공하는 key, value로  덮어쓴다.

(3) `.get(key[, default])` : key를 통해 value를 가져온다. key가 dictionary에 없어도 KeyError가 발생하지 않는다. 

(4) Dictionary comprehension

dict = `{key: value <조건문/반복문>}`

### 4.4 Set Method (세트 메소드)

(1) `.add(elem)` : element를 세트에 추가

(2) `.update(*others)` : 여러 개의 element를 set에 추가. 반드시 iterable한 값을 넣어야한다. 

(3) `.remove(elem)` : element를 세트에서 삭제하고, 없으면 KeyError가 발생.

(4) `.discard(elem)` : element를 세트에서 삭제하고, 리턴값이 None이라서 없어도 에러가 발생하지 않는다.

(5) `pop()` : 임의의 원소를 제거해 반환.

### 4.5 map, zip, filter

(1) `map(function, iterable)`

- iterable의 모든 원소에 function을 적용한 후 그 결과를 반환
- iterable type: list, dict, set, str, bytes, tuple, range
- return은 map_object 형태로 된다. 그래서 출력가능한 형태로 바꿔야 한다. list 같은 형태.

(2) `zip(*iterables)`

- 복수 iterable한 것들을 모아준다
- return은 튜플의 모음으로 구성된 zip object 형태로 된다. 출력가능한 형태로 바꿔야 한다.
- ex) `zip(list1, list2)` => output: (val1.1, val2.1), (val1.2, val2.2), ...
- 반드시 iterable object 끼리 길이가 같을 때 사용해야한다. 가장 짧은 것을 기준으로 구성하기 때문이다.
- 가장 긴 것을 기준으로 구성할 수 있다. 홀로 남은 값들은 fillvalue와 짝지어진다. `from itertools import zip_longest// zip_longest(iterable1, iterable2, fillvalue='args')`

(3) `filter(function, iterable)`

- iterable이 인자로 입력된 function의 반환된 결과가 참인 것들만 구성하여 반환
- true/false를 판단하는 function을 넣어야 한다
- return은 filter object 형태로 된다. 그래서 출력가능한 형태로 바꿔야 한다.



## 5. OOP(Object-Oriented Programming; 객체지향 프로그래밍)

- 객체 지향 프로그래밍은 컴퓨터 프로그래밍의 패러다임 중 하나
- 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것.
- 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다

### 5.1 클래스(Class)

- OOP의 기본적인 사용자 정의 데이터형 (User define data type)
- 같은 종류 또는 문제 해결을 위한 집단에 속하는 속성(attribute)와 행위(behavior)를 정의한 것
- 클래스는 다른 클래스 또는 외부 요소와 독립적으로 디자인 해야한다.

(1) 클래스 정의하기 (클래스 객체 생성하기)

- `class ClassName:`
- 선언과 동시에 클래스 객체가 생성됨
- 선언된 공간은 지역 스코프로 사용된다
- 정의된 속성 중 변수는 멤버 변수(data attribute)로 불리운다
- 정의된 함수는 메서드로 불리운다
- ClassName은 uppercamel convention을 사용한다

### 5.2 인스턴스(Instance)

- 클래스의 인스턴스/객체(실제로 메모리상에 할당된 것)
- 객체는 자신의 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)을 수행할 수 있다
- 객체의 행위는 클래스에 정의된 행위에 대한 정의(메서드)를 공유함으로써 메모리를 경제적으로 사용한다

(1) 인스턴스 생성하기

- 인스턴스 객체는 `ClassName()`을 호출함으로써 선언
- 인스턴스 객체와 클래스 객체는 서로 다른 이름공간을 가지고 있음
- **인스턴스 => 클래스 => 전역 순으로 탐색한다**
- 특별한 상황을 제외하고는, 클래스에서 인스턴스 메서드를 선언할 때에 반드시 `(self)` 가 첫번째 인자로 설정되어야 한다. 그래야 인스턴스 객체가 함수의 첫번째 인자로 전달되어 행위가 실행된다.
- ` self` 는 인스턴스 객체 자기자신을 의미

(2) 이름공간

- 클래스를 정의하면, 클래스 객체가 생성되고 해당되는 이름 공간이 생성된다
- 인스턴스를 생성하면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다
- 인스턴스의 속성이 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다
- 인스턴스에서 특정한 속성에 접근하게 되면 인스턴스 => 클래스 순으로 탐색한다

(3) 생성자/ 소멸자

- 생성자는 인스턴스 객체가 생성될 때 호출되는 함수

  ```python
  def __init__(self):
  	return bulabula
  ```

- 소멸자는 인스턴스 객체가 소멸되는 과정에서 호출되는 함수

  ```python
  def __del__(self):
  	return bulabula
  ```

- 양쪽에 언더스코어가 있는 메서드를 스페셜 메서드 혹은 매직 메서드라고 부른다

### 5.3 속성(Attribute)

- 클래스/인스턴스가 가지고 있는 속성(값)

(1) 클래스 변수

- 클래스의 속성

- 클래스 선언 블록 최상단에 위치

- 모든 인스턴스가 공유

- `Class.class_variable` 로 접근/할당한다

  ```python
  class TestClass:
  	class_variable1 = 'a'
  	class_variable2 = 'b'
  ```

(2) 인스턴스 변수

- 인스턴스의 속성
- 각 인스턴스들의 고유한 변수
- 메서드 정의에서 `self.instance_variable`로 접근/할당한다
- 인스턴스가 생성된 이후 `instance.instance_variable`로 접근/할당한다

```python
class TestClass:

def __init__(self, arg1, arg2):
	self.instance_var1 = arg1
	self.instance_var2 = arg2
	
def status(self):
	return self.instance_var1, self.instance_var2
```

### 5.4 메서드(Method)

- 클래스/인스턴스가 할 수 있는 행위(함수)

(1) 인스턴스 메서드

- 인스턴스가 사용할 메서드
- 정의 위에 어떠한 데코레이터가 없으면, 자동으로 인스턴스 메서드가 됩니다
- 첫 번째 인자로 `self`를 받도록 정의한다. 이 때, 자동으로 인스턴스 객체가 `self`가 된다

(2) 클래스 메서드

- 클래스가 사용할 메서드
- 정의 위에 `@classmethod` 데코레이터를 사용
- 첫 번째 인자로 클래스(`cls`) 를 받도록 정의한다. 이 때, 자동으로 클래스 객체가 `cls`가 된다.

(3) 스태틱(정적) 메서드

- 클래스가 사용할 메서드
- 정의 위에 `@staticmethod` 데코레이터를 사용
- 묵시적인 첫 번째 인자를 받지 않는다. 즉, 인자 정의는 자유롭게 한다.
- 어떠한 인자도 자동으로 넘어가지 않는다.
- 클래스 메서드와의 차이점은 권한 범위이다. 클래스메서드는 클래스 변수의 값을 변경할 수 없다. 프로그램을 만들 때, 사용자에게서 방어적으로 코드를 짜기 위해서 생긴 개념이다.

(4) 사용

- 인스턴스는 3가지 메서드에 모두 접근할 수 있다. 하지만 인스턴스에서 클래스메서드와 스태틱메서드는 호출하지 않아야 한다. 가능하다와 사용하다는 다르다.
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다
- 클래스도 3가지 메서드에 모두 접근할 수 있다. 하지만 클래스에서 인스턴스 메서든느 호출하지 않아야 한다. 가능하다와 사용하다는 다르다.
- 클래스가 할 행동은 다음 원칙에 따라 설계한다.
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 클래스 메서드로 정의한다
  - 클래스와 클래스 속성에 접근할 필요가 없다면 스태틱메서드로 정의한다

(5) 연산자 오버로딩(중복정의/ operator overloading)

- 파이썬에서  기본적으로 정의된 연산자를 직접적으로 정의하여 활용 할 수 있다.

- ```python
  +  __add__   
  -  __sub__
  *  __mul__
  <  __lt__
  <= __le__
  == __eq__
  != __ne__
  >= __ge__
  >  __gt__
  ```

- ```python
  n = (1).__add__(3)
  s = 'a'.__add__('b')
  l = [1].__add__(['x'])
  ```

### 5.5 상속

- 클래스에서 가장 큰 특징은 상속 기능을 가지고 있다는 것이다.

- 부모 클래스의 모든 속성이 자식 클래스에게 상속되므로 코드 재사용성이 높아진다.

- 공통된 속성이나 메서드를 부모 클래스에 정의하고, 이를 상속받아 다양한 형태의 인스턴스들을 만들 수 있다.

  ```python
  class DerivedClassName(BaseClassName):
  	code block
  ```

- **super()**

  - 자식 클래스에 메서드를 추가로 구현할 수 있다

  - 부모 클래스의 내용을 사용하고자 할때, `super()`를 사용한다

    ```python
    class BabyClass(ParentClass):
    	def method(self, arg):
    		super().method(arg)
    ```

- 메서드 오버라이딩 (재정의/ method overriding)

  - 메서드를 재정의 할 수 도 있다
  - 상속 받은 클래스에서 메서드를 덮어쓴다

- 상속 관계에서의 이름공간

  - 기존에 인스턴스 -> 클래스 순으로 이름공간을 탐색해나가는 과정에서 상속관계에 있으면 아래와 같이 확장된다
  - 인스턴스 -> 클래스 -> 전역
  - 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역

- 다중 상속

  - 두 개 이상의 클래스를 상속받는 경우, 다중 상속

  - `class BabyClass(ParentClass1, ParentClass2)`

    

## 6. 모듈

### 6.1 모듈 생성

- 모듈: 파이썬의 정의와 문장들을 담고 있는 파일
- 모듈 파일에는 확장자 `.py`를 붙인다
- 모듈 파일 안에 함수를 선언한다

### 6.2 모듈 사용

- 반드시 `import` 문을 통해 내장 모듈을 이름 공간에 가져와야 한다

- 패키지는 '점으로 구분된 모듈 이름'을 써서 파이썬의 모듈 이름 공간을 구조화 하는 방법. 예를 들어, `package_name.module_name()`

- 파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서는 `__init__.py` 파일이 필요하다.

- `import` 방법

  - `from 모듈명 import 어트리뷰트` : 특정 어트리뷰트만 꺼낸다
  - `from 모듈명 import *`: 모듈에 있는 변수, 함수, 클래스 전부 꺼낸다
  - `from 모듈명 import 어트리뷰트 as 이름` : 내가 지정하는 이름을 붙여 가져올 수 있다

- 파이썬 기본 모듈

  - math (함수 관련 함수): sum, max, min, abs, pow, round, divmod

  - | 함수                | 비고                            |
    | ------------------- | ------------------------------- |
    | math.ceil(x)        | 소수점 올림                     |
    | math.floor(x)       | 소수점 내림                     |
    | math.trunc(x)       | 소수점 버림                     |
    | math.copysign(x, y) | y의 부호를 x에 적용한 값        |
    | math.fabs(x)        | float 절대값 - 복소수 오류 발생 |
    | math.factorial(x)   | 팩토리얼 계산 값                |
    | math.fmod(x, y)     | float 나머지 계산               |
    | math.fsum(iterable) | float 합                        |
    | math.modf(x)        | 소수부 정수부 분리              |

  - | 함수                | 비고                                        |
    | ------------------- | ------------------------------------------- |
    | math.pow(x, y)      | x의 y 제곱의 결과                           |
    | math.sqrt(x)        | x의 제곱근의 결과                           |
    | math.exp(x)         | e^x 결과                                    |
    | math.log(x[, base]) | 밑을 base로 하는 logx (base default 값은 e) |

  - 삼각함수도 가능하다: sin, cos, tan, asin, ascos, aten, sinh, cosh, tanh, ashinh, acosh, atanh

    

  - `random`: 난수 발생관련 함수

  - `random`은 `seed`를 어떻게 설정하냐에 따라 생성되는 난수가 다르다.

    

  - `datetime`: 날짜 관련 모듈

  - | 형식 지시자(directive) | 의미                   |
    | ---------------------- | ---------------------- |
    | %y                     | 연도표기(00~99)        |
    | %Y                     | 연도표기(전체)         |
    | %b                     | 월 이름(축약)          |
    | %B                     | 월 이름(전체)          |
    | %m                     | 월 숫자(01~12)         |
    | %d                     | 일(01~31)              |
    | %H                     | 24시간 기준(00~23)     |
    | %I                     | 12시간 기준(01~12)     |
    | %M                     | 분(00~59)              |
    | %S                     | 초(00~61)              |
    | %p                     | 오전/오후              |
    | %a                     | 요일(축약)             |
    | %A                     | 요일(전체)             |
    | %w                     | 요일(숫자 : 일요일(0)) |
    | %j                     | 1월 1일부터 누적 날짜  |

  - | 속성/메소드 | 내용                 |
    | ----------- | -------------------- |
    | .year       | 년                   |
    | .month      | 월                   |
    | .day        | 일                   |
    | .hour       | 시                   |
    | .minute     | 분                   |
    | .second     | 초                   |
    | .weekday()  | 월요일을 0부터 6까지 |

  - `timedelta`: 시간 연산을 가능케 한다

  

## 7. Errors and Exceptions (예외처리)

### 7.1 Error

(1) Syntax Error (문법 에러)

- 파이썬이 읽어 들일 때 (parser)의 문제 발생 위치를 표현

(2) ZeroDivisionError: 0으로 나누기를 했을 때 발생하는 오류

(3) NameError: 정의되지 않은 이름을 불러왔을 때 발생

(4) TypeError: 코드에서 실행할 수 없는 class type을 사용했을 때 발생

(5) ValueError: 실행 코드에서 알맞는 value를 반환할 수 없을때 발생

(6) IndexError: 존재하지 않는 index를 불렀을 때 발생

(7) KeyError: 존재하지 않는 key를 불렀을 때 발생

(8) ModuleNotFoundError:  존재하지 않는 모듈을 불렀을 떄 발생

(9) ImportError: import 할 수 없을 때 발생

### 7.3 Exceptions (예외처리)

(1) 기본: `try ~ except ~`

```python
try:
	codeblock1
except 예외:
	codeblock2
```

- try 절이 실행된 후, 예외가 발생되지 않으면 except 없이 실행이 종료
- 예외가 중간에 발생하면, 남은 부분을 수행하지 않고 except가 실행

(2) 복수의 예외 처리

- 하나 이상의 예외를 모두 처리

- 괄호가 있는 tuple로 여러 개의 예외를 지정할 수 있다

- 에러가 순차적으로 수행됨으로, 가장 작은 범주부터 시작해야 한다

  ```python
  try:
  	codeblock 1
  except (예외1, 예외2):
   	codeblock 2
  ```

(3) 에러 문구 처리

```python
try:
	codeblock1
except 예외 as err:
	codeblock2
```

(4) `else`

- 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용한다

- 모든 except 절 뒤에 와야한다

- try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절하다

  ```python
  try:
  	numbers = [1, 2, 3]
  	number = numbers[2]
  except IndexError as err:
  	print(err)
  else:
  	print(number * 100)
  ```

(5) `finally`

- 반드시 수행해야하는 문장은 finally를 활용

- 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용

- 예외 발생 여부와 관계없이 try문을 떠날 때 항상 실행된다

  ```python
  try:
  	codeblock1
  except 예외:
  	codeblock2
  finally:
  	codeblock3
  ```

(6) `raise`

- 예외를 강제로 발생시킨다

  ```python
  try:
  	raise ValueError('error occured')
  except ValueError as err:
  	print(err)
  ```

(7) `assert`

- 예외를 발생시키는 방법

- 상태를 검증하는데 사용 되면 무조건 `AssetionError`가 발생

  `assert Boolean expression, error message`

- Bool 검증식이 거짓일 경우 발생

- `raise` 는 항상 예외를 발생시키고, 지정한 예외가 발생한다는 두가지 점에서 `assert`와 다르다

```python
def my_div(num1, num2):
    assert type(num1)==int and type(num2)==int, '둘 중 숫자가 아닌것이 있다.'
    
    try:
        result = num1 / num2
    except ZeroDivisionError as err:
            print(err)
    else:
        return result
```

