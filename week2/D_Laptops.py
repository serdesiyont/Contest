def solution():

    n = int(input())
    matrix = []
    for _ in range(n):
        l = list(map(int, input().split()))
        matrix.append(l)
    
    mp = matrix[n-1][0]
    mc = matrix[n-1][1]
    for i in range(n-1,-1,-1):
        
        if matrix[i][0] < mp and matrix[i][1] > mc: 
            print("Happy Alex")
            return
        elif matrix[i][0] < mp:
            mp = matrix[i][0]
            mc = matrix[i][1]
        
    print("Poor Alex")
solution()














# def solution():
#     n = int(input())
#     laptops = []
#     for _ in range(n):
#         a, b = map(int, input().split())
#         laptops.append([a, b])

#     laptops.sort(key=lambda x: x[0])

#     for i in range(n - 1):
#         if laptops[i][1] > laptops[i + 1][1]:
#             print("Happy Alex")
#             return

#     print("Poor Alex")

# solution()



