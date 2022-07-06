import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for i in range(N):
    cmd = input().split()
    x = 0
    if len(cmd) == 2:
        x = cmd[1]
    cmd = cmd[0]
    
    if cmd == "push":
        stack.append(x)
    elif cmd == "pop":
        if len(stack) > 0:
            result = stack.pop()
            print(result)
        else:
            print("-1")
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif cmd == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])


