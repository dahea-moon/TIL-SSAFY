# my와 real의 숫자 6개가 모두 같으면 1등
# my와 real의 숫자 중 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개 4등
# 3개 3등
# 나머지는 꽝

import random

my = random.sample(range(1, 46), 6)
print(my)
set(my)

# my = [23, 45, 26, 35, 3, 14]
# set(my)

real = {23, 3, 45, 26, 35, 14}
bonus = {34}

num_match_1 = len(set(my) & set(real))
num_match_2 = len(set(my) & set(bonus))

if num_match_1 == 6:
    print('1등')
elif num_match_1 == 5 and num_match_2 == 1:
    print('2등')
elif num_match_1 == 5:
    print('3등')
elif num_match_1 == 4:
    print('4등')
elif num_match_1 == 3:
    print('3등')
else:
    print('꽝')
