def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))


    pre = [0]*n
    """
        -6 -5 -3 0
         0   1   2   3


        10 3 4
              -5 8 1            

    """
    
    for i in range(k-1, n-k, -1):
        pre[i] = arr[i] - arr[i-1]
   
    if n == k:
        pre[0] = arr[0]

        for i in range(n-1):
            if pre[i] > pre[i+1]:
                print("No")
                return
        print("Yes")
        return

    print(pre)
    # for i in range(n-k+1, n-1):
    #     if pre[i] > pre[i+1]:
    #         print("NO")
    #         return
    
     
    

for _ in range(int(input())):
    solve()