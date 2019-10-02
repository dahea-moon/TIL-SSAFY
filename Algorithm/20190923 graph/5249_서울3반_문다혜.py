import sys
sys.stdin = open('5249.txt', 'r')

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(root1, root2):
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

    if rank[root1] == rank[root2]:
        rank[root2] += 1

def kruskal(nodes ,graph):
    global ans

    for node in nodes:
        make_set(node)

    for link in graph:
        v, u, w = link

        root1 = find(v)
        root2 = find(u)
        if root1 != root2:
            union(root1, root2)
            ans += w

    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [x for x in range(V+1)]
    graph = [tuple(map(int, input().split())) for _ in range(E)]
    graph = sorted(graph, key=lambda x: x[2])

    ans = 0
    kruskal(nodes, graph)

    print('#{} {}'.format(tc, ans))
