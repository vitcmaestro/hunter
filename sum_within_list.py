n = int(input(""))
lis = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(lis[i]+lis[j] == lis[k]):
                print(lis[i],lis[j],lis[k])
