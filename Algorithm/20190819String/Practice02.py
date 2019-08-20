def atoi(num):
    if isinstance(num, str):
        value = 0

        for i in range(len(num)-1, -1, -1):
            if ord(num[i]) >= ord('0') and ord(num[i]) <= ord('9'):
                digit = ord(num[i]) - ord ('0')
            else:
                break

        value = (value*10) + digit
        return value

    else:
        return False


def itoa(num):
    if isinstance(num, int):
        s = ''
        while True:
            digit = num % 10
            s = s + chr(digit + ord('0'))
            num = num // 10
            if num == 0:
                break

        char = ''
        for i in range(len(s)-1, -1, -1):
            char = char + s[i]

        return char
    else:
        return False


print(itoa(65))

