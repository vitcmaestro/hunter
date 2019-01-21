def frequency(i):
    c=0
    for j in lis:
        if(j == i):
            c+=1
    if(c>maxer):
        return c,i
    else:
        return maxer,ans
n = int(input(""))
lis = list(map(int,input().split()))
maxer = 0
for i in lis:
    maxer,ans = frequency(i)
if(maxer <= 1):
    print("unique")
else:
    print(ans)
