def solve():
    n = int(input()) 
    arr = list(map(int, input().split()))
    total = 0
    i = 0

    while i < n:
        cur = arr[i]

        while i < n and cur * arr[i] > 0:
            cur = max(cur, arr[i])
            i += 1
        
        total += cur
         
    
    print(total)
 

t = int(input())

for _ in range(t):
    solve()