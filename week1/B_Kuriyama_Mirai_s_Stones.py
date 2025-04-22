def solution():
    n = int(input())
    v = list(map(int, input().split()))
    u = v.copy()
    u.sort()
    m = int(input())
    cur = 0

    pre_u = [0]
    for i in range(n):
        cur += u[i]
        pre_u.append(cur)
    cur = 0
    pre_v = [0]
    for i in range(n):
        cur += v[i]
        pre_v.append(cur)



    for _ in range(m):
        t, l, r = map(int, input().split())
        if t == 1:
            print(pre_v[r] - pre_v[l-1])
        else:
            print(pre_u[r] - pre_u[l-1])

solution()