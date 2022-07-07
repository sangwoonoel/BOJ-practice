import sys

def read():
    return sys.stdin.readline().rstrip()

T = int(read())

for i in range(T):
    ps = input()
    cnt = 0
    for j in ps:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
