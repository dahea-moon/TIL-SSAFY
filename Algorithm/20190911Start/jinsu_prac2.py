data = '01D06079861D79F99F'
# data = '0F97A3'

output = ''
for tbit in data:
    try:
        t = int(tbit)
    except ValueError:
        t = ord(tbit) - ord('A') + 10

    for j in range(3, -1, -1):
        output += '1' if t & (1 << j) else '0'


for i in range(0, len(output), 7):
    tb = output[i:i+7]

    result = 0
    for idx, val in enumerate(tb):
        S = len(tb)
        if int(val):
            result += int(val) << ((S-1) - idx)

    print(result)
