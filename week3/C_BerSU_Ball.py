def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    pairs = 0
    paired_boys = [False] * n
    paired_girls = [False] * m

    for i in range(n):
        for j in range(m):
            if not paired_boys[i] and not paired_girls[j] and abs(a[i] - b[j]) <= 1:
                pairs += 1
                paired_boys[i] = True
                paired_girls[j] = True
                break

    print(pairs)
 
solve()