# words = input('입력 고고: ')

# # words의 첫 글자와 마지막 글자를 출력하라

# print(words[0], words[-1])

# import random

# length = random.choice(range(1, 100))
# unknown = list(range(length))

# print(unknown[length-1])
# print(unknown[-1])

# print(type(words))

# 자연수 n을 입력받고, 1 부터 n까지 출력하라

# numbers = input('자연수를 입력하라: ')
# numbers = int(numbers)
# #int()은 class type을 interger로 바꾸는 함수
# #''을 없앴을 때 int로 바꿀 수 있는 것은 10진수의 수이다.

# n = list(range(1, numbers+1))
# for numbers in n:
#     print(numbers)
#     numbers+=1
# print(type(numbers))

# print(n)
# print(type(n))

# for i in range(numbers-1):
#     print(i+1, end=',')

# number = int(input('숫자를 입력하세요: '))

# #짝수, 홀수를 구분하자

# if number % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# fizz buzz > 3의 배수에서 fizz 출력, 5배수에서 buzz, 15배수에서 fizzbuzz

numbers = int(input('숫자를 입력하세요: '))
for n in range(1, numbers+1):
    if n % 15 == 0:
        print('fizzbuzz')
    elif n % 5 == 0:
        print('buzz')
    elif n % 3 == 0:
        print('fizz')
    else:
        print(n)
