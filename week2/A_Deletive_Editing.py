def main():
    for _ in range(int(input())):
        s,t = input().split()
        
        
        from collections import Counter

        # Frequency of characters needed from t
        t_count = Counter(t)

        ans = []

        # Traverse s from end to start
        for ch in reversed(s):
            if t_count[ch] > 0:
                ans.append(ch)
                t_count[ch] -= 1

        # Since we went in reverse, reverse back to compare
        ans = ans[::-1]
        if ''.join(ans) == t:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
