import sys
sys.stdin = open('workline.txt', 'r')

for tc in range(1,4):
    V, E = map(int, input().split())
    links = list(map(int, input().split()))
    links = [links[i:i+2] for i in range(0,2*E,2)]

    link = {}
    for i in range(E):
        lv = []
        for v in range(E):
            if links[v][0] == links[i][0]:
                lv.append(links[v][1])
        link[links[i][0]] = lv

    for s in :

    stack = [s]
    visited = [1] + [0]*V

        while stack:
            visited[s] = 1
            if s not in link.keys():
                stack.append(s)
                return stack
            for i in link[stack[-1]]:
                if not visited[i]:
                    workline(link, i)


    print(workline(link, 1))