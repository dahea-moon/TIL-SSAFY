# 로또 추첨 풀이법

````python
# my와 real의 숫자 6개가 모두 같으면 1등
# my와 real의 숫자 중 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개 4등
# 3개 3등
# 나머지는 꽝

my = [1,2,3,4,5,6]

real = [1,2,3,4,5,7]
bonus = 8

match_count = 0
is_bonus = False       # is_bonus를 언제나 false라고 우선 저장해야, bonus 숫자가 맞지 않을 떄 is_bonus is not defined라는 오류가 안 뜬다. 모든 경우를 생각 해야한다.
for i in my:
    if i == bonus:
        is_bonus = True
    for j in real:           # 안에 있는 함수가 우선권이 있다
        if i == j:
            match_count += 1

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if is_bonus:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'           # print는 종결문으로 쓰지 않는다. 서버로 보내야하기 때문에. print는 debugging용.

print(result)

````

````python
# my와 real의 숫자 6개가 모두 같으면 1등
# my와 real의 숫자 중 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개 4등
# 3개 3등
# 나머지는 꽝

my = [1,2,3,4,5,6]

real = [1,2,3,4,5,7]
bonus = 8

match_count = 0

for i in my:
    for j in real:           # 안에 있는 함수가 우선권이 있다
        if i == j:
            match_count += 1

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝'           

# print는 종결문으로 쓰지 않는다. 서버로 보내야하기 때문에. print는 debugging용.

print(result)

````

````python
# my와 real의 숫자 6개가 모두 같으면 1등
# my와 real의 숫자 중 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개 4등
# 3개 3등
# 나머지는 꽝

import random

my = random.sample(range(1, 46), 6)
print(my)

# my = [23, 45, 26, 35, 3, 14]
# set(my)

#[1,2,3] > LIST / {1,2,3} > SET / (1,2,3) > TUPLE / {'A':'a'} > dict
real = {23, 3, 45, 26, 35, 14}
bonus = {34}

num_match_1 = len(set(my) & real) # .intersection == & == 교집합
num_match_2 = len(set(my) & bonus)

if num_match_1 == 6:
    result = '1등'
elif num_match_1 == 5 and num_match_2 == 1:
    result = '2등'
elif num_match_1 == 5:
    result = '3등'
elif num_match_1 == 4:
    result = '4등'
elif num_match_1 == 3:
    result = '5등'
else:
    result = '꽝'

print(result)

````

