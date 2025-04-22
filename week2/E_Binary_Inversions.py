
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    un = arr.copy()
    def counter(n, arr: list):
        seen = 0
        inversions = 0
        l, r = 0,1
        while r < n:
            while r < n and arr[r] == 0 and arr[l] == 1:
                inversions += 1 + seen*1
                r  += 1
            if r < n -1 and arr[r] == 1 and arr[l] == 0:
                l += 1
                r += 1
            else:
                if r < n and arr[r] == 1:
                    seen += 1
                l = r
                r += 1
    
        return inversions

    without_flip = counter(n, arr)

    for a in range(n):
        if arr[a] == 0:
            arr[a] = 1
            break
    
    flip = counter(n, arr)

    for a in range(n-1, -1, -1):
        if un[a] == 1:
            un[a] = 0
            break

    back = counter(n, un)
    print(max(without_flip, flip, back))


t = int(input())
for _ in range(t):
    solution()








































# def solve_optimized():
#     n = int(input())
#     a = list(map(int, input().split()))

#     max_inversions = count_initial_inversions(a)
#     ones_left, zeros_right = precompute(a)

#     for k in range(n):
#         current_inversions = count_initial_inversions(a) # Recalculate for clarity, but can be optimized further

#         if a[k] == 0:
#             # Flipping 0 to 1 increases inversions by zeros to the right
#             inversions_after_flip = current_inversions + zeros_right[k]
#             max_inversions = max(max_inversions, inversions_after_flip)
#         else:  # a[k] == 1
#             # Flipping 1 to 0 changes inversions by (ones to the left) - (zeros to the right)
#             inversions_after_flip = current_inversions + ones_left[k] - zeros_right[k]
#             max_inversions = max(max_inversions, inversions_after_flip)

#     print(max_inversions)

# def count_initial_inversions(arr):
#     n = len(arr)
#     inversions = 0
#     ones_count = 0
#     for x in arr:
#         if x == 1:
#             ones_count += 1
#         else:
#             inversions += ones_count
#     return inversions

# def precompute(arr):
#     n = len(arr)
#     ones_left = [0] * n
#     zeros_right = [0] * n

#     ones = 0
#     for i in range(n):
#         ones_left[i] = ones
#         if arr[i] == 1:
#             ones += 1

#     zeros = 0
#     for i in range(n - 1, -1, -1):
#         zeros_right[i] = zeros
#         if arr[i] == 0:
#             zeros += 1

#     return ones_left, zeros_right

# t = int(input())
# for _ in range(t):
#     solve_optimized()


