# 이 풀이 말고 백준 상위 풀이 잘 이해가 안돼
#만약 디큐를 못쓴다면??

from collections import deque

q = deque()

N = int(input())

for i in range(N):
    q.appendleft(i+1)

while len(q) > 1:
    q.pop()
    result = q.pop()
    q.appendleft(result)
print(q[0])