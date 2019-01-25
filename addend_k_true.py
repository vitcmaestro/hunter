n,k = map(int,input().split())
a = list(map(int,input().split()))
m=0
for i in range(n):
    for j in range(n):
        if(a[i]+a[j] == k):
            m = 1
if(m == 1):
    print("YES")
else:
    print("NO")
