import sys
sys.stdin = open('test.txt', 'r')

def up(cr, cc, rooms, tmp):
    while 1:
        cr -= 1
        if rooms[cr][cc] == 6 or cr < 0:
            break
        elif 0 < rooms[cr][cc] < 6:
            pass
        else:
            rooms[cr][cc] = 7
            tmp += [(cr, cc)]

def right(cr, cc, rooms, tmp):
    while 1:
        cc += 1
        if cc == m or rooms[cr][cc] == 6 :
            break
        elif 0 < rooms[cr][cc] < 6:
            pass
        else:
            rooms[cr][cc] = 7
            tmp += [(cr, cc)]


def down(cr, cc, rooms, tmp):
    while 1:
        cr += 1
        if cr == n or rooms[cr][cc] == 6 :
            break
        elif 0 < rooms[cr][cc] < 6:
            pass
        else:
            rooms[cr][cc] = 7
            tmp += [(cr, cc)]

def left(cr, cc, rooms, tmp):
    while 1:
        cc -= 1
        if rooms[cr][cc] == 6 or cc < 0:
            break
        elif 0 < rooms[cr][cc] < 6:
            pass
        else:
            rooms[cr][cc] = 7
            tmp += [(cr, cc)]


# 중복조합이 입력되면 rooms에서 바꿔서 사각지대 크기 출력
def search(rooms, cctv_dir, cctvs, tmp):
    global cctvs_cnt, cctvs_pos, mini
    for i in range(cctvs_cnt):
        if cctvs[i] == 1:
            if cctv_dir[i] == 0:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 1:
                cr, cc = cctvs_pos[i]
                right(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 2:
                cr, cc = cctvs_pos[i]
                down(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 3:
                cr, cc = cctvs_pos[i]
                left(cr, cc, rooms, tmp)
        elif cctvs[i] == 2:
            if cctv_dir[i] == 0:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 1:
                cr, cc = cctvs_pos[i]
                right(cr, cc, rooms, tmp)
                left(cr, cc, rooms, tmp)
            else:
                return
        elif cctvs[i] == 3:
            if cctv_dir[i] == 0:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
                right(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 1:
                cr, cc = cctvs_pos[i]
                right(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 2:
                cr, cc = cctvs_pos[i]
                down(cr, cc, rooms, tmp)
                left(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 3:
                cr, cc = cctvs_pos[i]
                left(cr, cc, rooms, tmp)
                up(cr, cc, rooms, tmp)
        elif cctvs[i] == 4:
            if cctv_dir[i] == 0:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
                right(cr, cc, rooms, tmp)
                left(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 1:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
                right(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 2:
                cr, cc = cctvs_pos[i]
                right(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
                left(cr, cc, rooms, tmp)
            elif cctv_dir[i] == 3:
                cr, cc = cctvs_pos[i]
                left(cr, cc, rooms, tmp)
                up(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
        else:
            if cctv_dir[i] == 0:
                cr, cc = cctvs_pos[i]
                up(cr, cc, rooms, tmp)
                right(cr, cc, rooms, tmp)
                down(cr, cc, rooms, tmp)
                left(cr, cc, rooms, tmp)
            else:
                return

    safe = 0
    for x in range(n):
        for y in range(m):
            if rooms[x][y] == 0:
                safe += 1

    # 함수 return 값이 mini 값과 비교
    if safe < mini:
        mini = safe
    return


# 중복조합 만들기
# 0: 상, 1: 오, 2: 하, 3: 왼
def combinations(idx, cctv_dir, cctvs_cnt):
    global cctvs, rooms
    if idx == cctvs_cnt:
        tmp = []
        search(rooms, cctv_dir, cctvs, tmp)
        for t in tmp:
            p, q = t
            rooms[p][q] = 0
        return

    cctv_dir[idx] = 0
    combinations(idx+1, cctv_dir, cctvs_cnt)

    cctv_dir[idx] = 1
    combinations(idx+1, cctv_dir, cctvs_cnt)

    cctv_dir[idx] = 2
    combinations(idx+1, cctv_dir, cctvs_cnt)

    cctv_dir[idx] = 3
    combinations(idx+1, cctv_dir, cctvs_cnt)

# 정보 input
n, m = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]

cctvs_pos = []
cctvs = []
for r in range(n):
    for c in range(m):
        if 0 < rooms[r][c] < 6:
            cctvs += [rooms[r][c]]
            cctvs_pos += [(r, c)]

cctvs_cnt = len(cctvs)
mini =9999999
cctv_dir = [0]*cctvs_cnt

# 중복조합 만들기
combinations(0, cctv_dir, cctvs_cnt)
print(mini)

