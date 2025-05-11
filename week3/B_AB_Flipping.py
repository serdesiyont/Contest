def solve():
    n = int(input())
    s = input()
    swapped = set()
    max_op = 0

    for i in range(n-1):
        if s[i] == 'A' and s[i+1] == 'B' and i not in swapped:
            max_op += 1
            swapped.add(i)
    print(max_op)





t = int(input())
for _ in range(t):
    solve()