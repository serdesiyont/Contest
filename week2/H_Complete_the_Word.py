def solution():
    s = input()
    n = len(s)

    if n < 26:
        print("-1")
        return

    i = 0
    j = 25
    mp = {}
    for k in range(26):
        mp[s[k]] = mp.get(s[k], 0) + 1

    while j < n:
        f = True
        sum_zeros = 0

        for char_code in range(ord('A'), ord('Z') + 1):
            char = chr(char_code)
            if mp.get(char, 0) > 1:
                f = False
                break
            elif mp.get(char, 0) == 0:
                sum_zeros += 1

        if not f:
            mp[s[i]] -= 1
            i += 1
            j += 1
            if j < n:
                mp[s[j]] = mp.get(s[j], 0) + 1
            continue

        if sum_zeros == mp.get('?', 0):
            v = []
            for char_code in range(ord('A'), ord('Z') + 1):
                char = chr(char_code)
                if mp.get(char, 0) == 0:
                    v.append(char)
            v.reverse()

            s_list = list(s)
            v_idx = 0
            for k in range(i, j + 1):
                if s_list[k] == '?':
                    s_list[k] = v[v_idx]
                    v_idx += 1
            s = "".join(s_list)

            s_list = list(s)
            for k in range(n):
                if s_list[k] == '?':
                    s_list[k] = 'A'
            s = "".join(s_list)

            print(s)
            return

        if j < n - 1:
            mp[s[i]] -= 1
            i += 1
            j += 1
            mp[s[j]] = mp.get(s[j], 0) + 1
        else:
            break

    print("-1")

solution()