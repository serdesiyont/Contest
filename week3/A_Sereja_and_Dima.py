from collections import deque
n = int(input())
arr = deque()
for i in (input().split()):
    arr.append(int(i))

s = 0
d = 0

for i in range(n):
    if i % 2 == 0:
        if arr[0] > arr[-1]:
            s += arr[0]
            arr.popleft()
        else: 
            s += arr[-1]
            arr.pop()
    else:
        if arr[0] > arr[-1]:
            d += arr[0]
            arr.popleft()
        else: 
            d += arr[-1]
            arr.pop()
print(s, d)