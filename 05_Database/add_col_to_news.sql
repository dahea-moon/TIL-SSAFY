# 테이블 뉴스에 새로운 열인 created_at을 추가하는데 생성시간을 넣는다
# 이 열은 not null의 설정을 가지고 있는데, 열 생성 전에 만들어진 행 값에는 1을 넣는다고
# default 값을 정해놓는다

ALTER TABLE news
ADD COLUMN created_at
DATETIME NOT NULL DEFAULT 1;
