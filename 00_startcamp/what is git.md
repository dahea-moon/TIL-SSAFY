# what is git

git: scm (source code manager) / vcs (version control system)

버전 관리를 해주는 cctv



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

`git remote add origin`:  내 백업은 여기로 보내

`git remote -v`: 내 백업 공간은 어디야?

`git push origin master`:  origin으로 백업 해줘

`git add -A`: 여러개를 한 번에 저장할게

`git add . ` : 여러 개를 한 번에 저장할게

#tab 누르면 파일명을 쉽게 쓸 수 있음

## 내 git sign

`git config-global user.email "email"`

`git config-global user.name "name"`

