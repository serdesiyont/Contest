n = int(input())
arr = list(map(lambda x: int(x), input().split()))

arr.sort()

height = 0
towers = 0

"""
5 6 6 7

"""

l = r = 0

while r < n:
    r += 1
    length = 1
    while r < n and arr[l] == arr[r]:
        r += 1
        length += 1
    
    height = max(height, length)
    towers += 1
    l = r
    

print(height, towers)
    

