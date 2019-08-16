# algorithm

## 언어의 방식

### compiler 방식

- c, c++, java
- compile & Link 과정이 있다
- compile하면 object code 형태로 나오고, 이를 exe, dill과 같은 실행파일로 만들기 위해 link를 함
- 실행파일이 만들어지면 운영체제가 실행시키는 것
- 변수의 데이터 타입을 먼저 선언해야한다

### interpreter 방식

- python
- compile 과정이 없다
- run시키면 바로 실행이 되서 결과를 보여준다
- interpreter가 실행시키는 것
- 데이터 타입을 먼저 선언하지 않아도 됨
- compiler보다 속도가 많이 늦다
- 같은 기능의 프로그램을 짜더라도 interpreter 언어가 짜는 시간이 더 빠르다. library를 많이 제공해주기 때문에. 즉, 개발 생산성이 좋다는 뜻.
- python은 구조적으로 대용량 데이터를 고려해서 설계되었다.

### script 언어

- javascript, php, jsp
- 특정 목적을 위해 만들어진 언어
- interpreter 방식을 기초로해서 만들어짐
- sciprt 언어가 아니면 general purpose