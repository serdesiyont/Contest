
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