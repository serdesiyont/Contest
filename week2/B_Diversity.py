
def solution():
    word = input()
    k = int(input())
    n = len(word)

    if k > n:
        print("impossible")
        return
    
    seen = set(word)
     
    u = len(seen)
    if u >= k:
        print(0)
        return
    c = k - u
    print(c)
     

solution()

