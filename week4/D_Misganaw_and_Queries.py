s = input()
n = len(s)
pre = [0]
"......   [0,1,2,3,4,5]"
for i in range(1,n):
    pre.append(pre[-1] + (1 if s[i] == s[i-1] else 0))


for _ in range(int(input())):
    l, r = map(lambda x: int(x)-1, input().split())
     
    
    print(pre[r]-pre[l])
