import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())

    icp = {'+':1, '*':2, '(':3}
    isp = {'(':0, '+':1, '*':2}

    
