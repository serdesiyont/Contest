n = int(input())
arr = list(map(lambda x: abs(int(x)), input().split()))

arr.sort()

print(arr[0])
