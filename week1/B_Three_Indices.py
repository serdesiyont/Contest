# def solution():
    
    
    
#         l = int(input())
#         p = list(map(int, input().split()))
        
#         for i in range(l-1):
#             if(p[i]>p[i-1] and p[i]>p[i+1]):
#                    print("YES")
#                    print(i,i+1, i+2)
#                    return
#         print("No")
# tests = int(input())
# for _ in range(tests):
#     solution()

    

# def solve():
#     n = int(input())
#     p = list(map(int, input().split()))

#     for i in range(1, n - 1):
#         if p[i] > p[i - 1] and p[i] > p[i + 1]:
#             print("YES")
#             print(i, i + 1, i + 2)
#             return

#     print("NO")
 
# tests = int(input())
# for _ in range(tests):
#     solve()

 
    

tests=int(input())

for i in range(tests):
    n=int(input())
    p=[int(x) for x in input().split()]
    found=False
    for i in range(1,n-1):
        if p[i]>p[i-1] and p[i]>p[i+1]:
            found=True
            print("YES")
            print(i,i+1,i+2)
            break
    if not found:
        print("NO")



 