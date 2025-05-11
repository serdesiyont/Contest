def solve():
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))


    

    l = r = 0
    count = 0
    while r < n:
         
        
        s = 0
        while r < n and arr[r] <= q:

            if r-l+1 >= k:
                s += 1
                count += s
            r += 1
        
        r += 1
        l = r
    
    print(count)


for _ in range(int(input())):
    solve()



    