n, s = map(int, input().split())
arr = list(map(int, input().split()))

l = r = 0
cur = 0
longest = 0
while r < n:
    cur += arr[r]

    while  cur > s:
        cur -= arr[l]
        l += 1
    longest = max(longest, r-l+1)
    r += 1
print(longest)