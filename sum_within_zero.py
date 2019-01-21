n = int(input(""))
lis = list(map(int,input().split()))
miner = 100
c =0
for i in range(n):
    for j in range(i+1,n):
        if(lis[i]+lis[j] == 0):
            print(lis[i]+lis[j])
            c+=1
        else:
            if(lis[i]+lis[j] < miner):
                miner = lis[i]+lis[j]
                a = lis[i] 
                b = lis[j]
if(c ==0):
    print(a,b)
