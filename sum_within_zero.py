n = int(input(""))
lis = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if(lis[i]+lis[j] == 0):
            print(lis[i],lis[j])
