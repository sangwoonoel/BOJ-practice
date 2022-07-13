#다시 풀어보기
import sys
from collections import deque

def scan():
    return sys.stdin.readline().rstrip()

N = int(scan())
post = scan()
oper = '+-*/'

dic = {}
stack = []
num = deque()

for i in range(N):
    num.append(int(scan()))

for i in post:
    if i not in dic and i not in oper:
        dic[i] = num.popleft()

for i in post:
    if i not in oper:
        stack.append(dic[i])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)

print(f"{stack[0]:.2f}")