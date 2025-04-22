# # def solution():
# #     t = int(input())

# #     for _ in range(t):
# #         n, k = map(int, input().split())
# #         c = input()
# #         least = float("inf")
# #         shifts = n - k
# #         for i in range(shifts+1):
# #             w = c[i:k+i]
# #             least = min(least, w.count("W"))
# #         print(least)
        

# # solution()



# def solution():
#     n, k = map(int, input().split())
#     c = input()
    
#     least = k  
    
#     for i in range(n - k + 1):
#         window = c[i:i+k]
#         white_count = window.count('W')
#         least = min(least, white_count)
    
#     print(least)

# t = int(input())
# for _ in range(t):
#     solution()res = min(res, curr)



def solve():
    n, k = map(int, input().split())
    s = input()
    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        curr = 0
        if s[i - 1] == 'W':
            curr = 1
        preSum[i] = preSum[i - 1] + curr

    res = float('inf')
    for i in range(k, n + 1):
        curr = preSum[i] - preSum[i - k]
        res = min(res, curr)
        
    print(res)

t = int(input())
for _ in range(t):
    solve()







# def solution():
#     n, k = map(int, input().split())
#     c = input()
     
    
#     l = 0
#     w = c[:k].count("W")
#     r = w
#     while k < n:
         
#         r  = min(r, w)
#         if c[l] == "W":
#             w -= 1
#         elif k < n and c[k] == "W":
#             w += 1
#         l += 1
#         k +=1
#     print(r)


# t = int(input())

# for _ in range(t):
#     solution()
        

