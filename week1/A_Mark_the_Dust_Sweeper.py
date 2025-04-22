 






















    
def solution():
    n = int(input())
    a = list(map(int, input().split()))

    operations = 0
    first_nonzero = -1
    for i in range(n - 1):
        if a[i] > 0:
            if first_nonzero == -1:
                first_nonzero = i
            operations += a[i]
    if first_nonzero != -1:
        for i in range(first_nonzero, n - 1):
            if a[i] == 0 and i < n - 1:
                operations += 1

    print(operations)


t = int(input())
for _ in range(t):
    solution()