n,k = map(int,input().split())
a = list(map(int,input().split()))
j=0
for i in range(n):
    for j in range(i,n):
        if(a[i]+a[j] == k):
            print("YES")
            j= 1
            i = n-1
            j= n-1
if(j ==0):
    print("NO")
