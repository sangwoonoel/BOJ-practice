import sys
from collections import deque


def scan():
    return sys.stdin.readline().rstrip()


N = int(scan())

q = deque()

for i in range(N):
    cmd = scan().split(" ")
    if len(cmd) == 2:
        x = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        q.append(x)
    elif cmd == "pop":
        if q:
            result = q.popleft()
            print(result)
        else:
            print(-1)
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
