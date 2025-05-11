# from collections import defaultdict
# def solve():
    
#     n, k, d = map(int, input().split())
#     arr = list(map(int, input().split()))
#     count = defaultdict(int)
    
#     for i in range(d):
#         count[arr[i]] += 1
#     min_ = len(count.keys())

#     for i in range(1, n-d):
#         count[arr[i-1]] -= 1
#         count[arr[i+d]] += 1

#         if count[arr[i-1]] == 0: count.pop(arr[i-1])

#         min_ = min(min_, len(count.keys()))

#     print(min_)



from collections import defaultdict

def solve():
        n, k, d = map(int, input().split())
        a = list(map(int, input().split()))

        freq = defaultdict(int)
        unique = 0

        for i in range(d):
            if freq[a[i]] == 0:
                unique += 1
            freq[a[i]] += 1

        min_unique = unique

        for i in range(d, n):
            freq[a[i - d]] -= 1
            if freq[a[i - d]] == 0:
                unique -= 1

            # Add a[i]
            if freq[a[i]] == 0:
                unique += 1
            freq[a[i]] += 1

            min_unique = min(min_unique, unique)
        print(min_unique)



for _ in range(int(input())):
    solve()



