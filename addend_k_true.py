n,k = map(int,input().split())
a = list(map(int,input().split()))
j=0
for i in range(n):
    for j in range(i+1,n):
        if(a[i]+a[j] == k):
            print(a[i][j])
            j= 1
if(j == 1):
    print("YES")
else:
    print("NO")
