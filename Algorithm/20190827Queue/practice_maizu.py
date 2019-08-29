q = [0]*100
f = r = -1
candis = 20
studcan = [1]*20

sn = 1
nextsn= 2

r += 1
q[r] = sn

while candis > 0:
    f += 1
    sn = q[f]
    candis -= studcan[sn]
    studcan[sn] += 1

    if candis <= 0:
        print(sn)
        break

    r += 1
    q[r] = sn
    r += 1
    q[r] = nextsn

    nextsn += 1