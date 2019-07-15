# CLI

CLI is a command line program that accepts text input to execute operating system functions.

In the 1960s, using only computer terminals, this was the only way to interact with computers.

In the 1970s an 1980s, command line input was commonly used by Unix systems and PC systems like MS-DOS and Apple DOS.

Today, with graphical user interfaces (GUI), most users never use command-line interfaces (CLI).

However, CLI is still used by software developers and system administrators to configure computers, install software, and access features that are not available in the graphical interface.



## git command

띄어쓰기: 명령어 구분

'-' : 옵션

mkdir: directory 만들기

touch: file 만들기

touch file1 file2 file3 하면 여러개 만들기 가능. 띄어쓰기로 파일 구분. (지우기도 가능)

rm: 삭제하기

file 확장명을 정해줘야 오픈 프로그램이 정해짐

/는 폴더의 상징. 그러나 지울때는 rm -r dic./해야 지워짐.

cd(change directory): 이동하기

cd .. : 상위 폴더로 이동

cd - : 뒤로가기

cd dic.: dic.로 이동

tab을 누르면 file, dic의 이름 자동완성을 지원해줌

pwd: 나의 현재 위치 알려줘

echo == print

**ctrl + c : 취소하기**

**clear: 화면 정리 (ctrl + l)**

man echo: git command manual 

ctrl + u: 명령어 전체 삭제

ctrl + back space: 단어 단위 삭제

ctrl + d:  종료

ls : 현재 위치에서 있는거 보여줘

ls -a: 현재 위치에 있는거 전부 다 보여줘

./ : 내 자리

../ :  내 윗 자리

touch .file: hidden file 만들기

같은 name space에서는 같은 name의 file을 만들 수 없음

cp file: file 복사하기

cp original file new name: original file을 new name으로 복사하겠다

cp file ../ : 상위 폴더에 file을 복사하겠다

cp file dic : 이 dic에 file을 복사하겠다

cp file dic new name : 이 dic에 file을 new name으로 복사하겠다

mv file dic : file을 dic으로 이동하겠다

mv dic1 file dic2 : dic 1에 있는 file을 dic 2에 이동하겠다

mv file1 file2: file1을 file2로 이름 바꾸겠다

sudo(super user do): 지금부터 내 명령어는 super user의 명령이다. 막아놓은 일까지 할 수 있다. 

그러나 위험하니까 쓰지말자.

rm -f: 강제로 지우겠다

'-f' == force ; 강제 옵션

rm -rf dic: dic과 그 안의 파일을 전부 다 지우겠다

git itin: 버전 관리를 시작하겠다. master가 나타남.

rm -r .git : .git 폴더를 삭제한다. git에 저장한 기록이 지워지고, master 표시가 없어진다.

'-p' : 한 방에 하겠다

disc에 저장할 수 있는 것은 파일과 폴더 밖에 안된다.

disc의 최상단 폴더인 시작폴더는 '/'로 상징된다. c drive 보다도 상위 폴더인 컴퓨터의 최상단 폴더.

'~' : home 이라는 상징.  cd 만 치면 ~ 으로 이동한다.



## 디스크와 메모리

디스크와 메모리는 다르다.

메모리 == 작업테이블

메모리는 무한하지 않다. 크기가 정해져있다.

메모리의 크기는 컴퓨터 마다 다른데, 메모리가 클수록 컴퓨터의 성능이 좋다. 

사람 = cpu (프로세서), 작업테이블 = ram

ram == random access memory

메모리는 휘발성이다. 영속성이 없다. 그래서 빠르다. 

디스크는 영속성이 있다. (물론 날라가기도 한다)



