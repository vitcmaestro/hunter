n,k = map(int,input().split())
lis =[]
ans=[]
for i in range(n):
    temp = list(map(int,input().split()))
    lis.append(temp)
for j in range(k):
    c=0
    for i in range(1,n):
        for l in range(k):
            if(lis[0][j] == lis[i][l]):
                c+=1
    if(c == n-1):
        ans.append(lis[0][j])
for i in range(len(ans)):
    if(i==0):
        print(ans[i],end="")
    else:
        print("",ans[i],end="")
