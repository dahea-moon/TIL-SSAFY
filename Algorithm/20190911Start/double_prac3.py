password = {'001101': 0, '010011':1, '111011':2, '110001':3, '100011':4, '110111':5,
            '001011':6, '111101':7, '011001':8, '101111':9}
pwdkey = list(password.keys())

def pwd(output):
    if len(output) < 6:
        return

    for i in range(len(output)-1, -1, -1):
        if output[i] == '1':
            chk = output[i-5:i+1]
            if chk in pwdkey:
                print(password.get(chk))
                output = output[0:i-5]
                return pwd(output)

data = '0269FAC9A0'
output = ''
for tbit in data:
    try:
        t = int(tbit)
    except ValueError:
        t = ord(tbit) - ord('A') + 10

    for j in range(3, -1, -1):
        output += '1' if t & (1 << j) else '0'

print(output)

pwd(output)
