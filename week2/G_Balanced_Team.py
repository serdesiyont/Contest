n = int(input())
sk = list(map(int, input().split()))

sk.sort()
l, r = 0,1
m = 0
while r < n:
    while r < n and sk[r] - sk[l] <= 5:
        m = max(m, r-l+1)
        r += 1
    l = r
    r += 1

print(m)