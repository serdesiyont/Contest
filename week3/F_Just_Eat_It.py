# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))

    
#     y_flag = True
#     for i in a:
#         if i < 0:
#             y_flag = False
#             break
    
#     if y_flag:
#         print("YES")
#         return
#     y = sum(a)

#     prefix = 0
#     max_ = -float('inf')

#     for r in range(n-1):
#         prefix += a[r]

#         max_ = max(max_, prefix)

#         if prefix < 0:
#             prefix = 0
    
#     if a[-1] > 0:
#         max_ += a[-1]
    
#     if y <= max_:
#         print("NO")
#     else:
#         print("YES")


# for _ in range(int(input())):
#     solve()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    y = sum(a)

    y_flag = True
    for i in a:
        if i < 0:
            y_flag = False
            break

    if y_flag:
        print("YES")
        return

    prefix = 0
    max_ = -float('inf')

    for r in range(n - 1):
        prefix += a[r]
        max_ = max(max_, prefix)
        if prefix < 0:
            prefix = 0
    prefix = 0
    for r in range(1,n):
        prefix += a[r]
        max_ = max(max_, prefix)
        if prefix < 0:
            prefix = 0

    suffix = 0
    for l in range(n - 1, 0, -1):
        suffix += a[l]
        max_ = max(max_, suffix)
        if suffix < 0:
            suffix = 0
    suffix = 0
    for l in range(n - 2, -1, -1):
        suffix += a[l]
        max_ = max(max_, suffix)
        if suffix < 0:
            suffix = 0

    

    if y > max_:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()