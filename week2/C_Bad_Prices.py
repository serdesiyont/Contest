def solution():
    n = int(input())
    sold = list(map(int, input().split()))

    bad = 0
    cur = sold[n-1]
    for i in range(n-2, -1, -1):
        if sold[i] > cur:
            bad += 1
        
        else:
            cur = sold[i]
    
    print(bad)
        
t = int(input())
for _ in range(t):
    solution()







# def solution():
#     n = int(input())
#     a = list(map(int, input().split()))

#     bad_days_count = 0
#     min_price_so_far = float('inf')

#     for i in range(n - 1, -1, -1):
#         if a[i] > min_price_so_far:
#             bad_days_count += 1
#         min_price_so_far = min(min_price_so_far, a[i])
#     print(bad_days_count)

# t = int(input())
# for _ in range(t):
#     solution()         
        
 

