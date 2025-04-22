def solution():
    n = int(input())
    l, r = 0, n - 1
    candies = list(map(int, input().split()))
    ls = candies[l]
    rs = candies[r]
    c = 0

    while l<r:
        if ls == rs:
            c = n-r + l+1
            l += 1
            r -= 1
            ls += candies[l]
            rs += candies[r]
        
        elif ls > rs:
            r -= 1
            rs += candies[r]
        
        else:
            l += 1
            ls += candies[l]

    print(c)



tests = int(input())

for _ in range(tests):
    solution()