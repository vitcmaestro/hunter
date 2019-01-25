n = int(input(""))
a = list(map(int,input().split()))
maxer = a[0]
for j in range(1,n):
    summer = a[0]
    for i in range(1,j):
        summer =summer + a[i]
    if(summer > maxer):
        maxer = summer
print(maxer)
