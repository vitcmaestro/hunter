n = int(input(""))
a = list(map(int,input().split()))
maxer = a[0]
for j in range(1,n):
    summer = a[0]
    for i in range(1,j):
        summer =summer + a[i]
    if(summer > maxer):
        maxer = summer
maxer1 = a[n-1]
for j in range(n-1,-1,-1):
    summer1 = a[-1]
    for i in range(n-2,j,-1):
        summer1 =summer1 + a[i]
    if(summer1 > maxer1):
        maxer1 = summer1
print(max(maxer,maxer1))
