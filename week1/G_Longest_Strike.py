# def solve():
#     n, k = map(int, input().split())
#     v = list(map(int, input().split()))
    
#     from collections import defaultdict

#     freq = defaultdict(int)
#     for i in v:
#         freq[i] += 1

#     valid = [key for key in sorted(freq) if freq[key] >= k]

#     if not valid:
#         print(-1)
#         return

#     max_len = -1
#     st = valid[0]
#     l = r = None

#     for i in range(1, len(valid)):
#         if valid[i] - 1 != valid[i - 1]:
#             if valid[i - 1] - st > max_len:
#                 max_len = valid[i - 1] - st
#                 l, r = st, valid[i - 1]
#             st = valid[i]

#     # Handle last segment
#     if valid[-1] - st > max_len:
#         l, r = st, valid[-1]

#     print(l, r)


# t = int(input())
# for _ in range(t):
#     solve()


 
from collections import Counter

def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))

    freq = Counter(v)
    valid = sorted([x for x in freq if freq[x] >= k])

    if not valid:
        print(-1)
        return

    max_len = -1
    l = r = valid[0]
    start = valid[0]

    for i in range(1, len(valid)):
        if valid[i] != valid[i - 1] + 1:
            if valid[i - 1] - start > max_len:
                max_len = valid[i - 1] - start
                l, r = start, valid[i - 1]
            start = valid[i]

    # Final check for last segment
    if valid[-1] - start > max_len:
        l, r = start, valid[-1]

    print(l, r)

for _ in range(int(input())):
    solve()


