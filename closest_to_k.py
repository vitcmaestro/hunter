n,k = map(int,input("").split())
lis = list(map(int,input().split()))
ans = []
i = 0
j=1
while(i<3):
    temp = k+j
    if(temp in lis):
        ans.append(temp)
        i+=1
    temp1 = k-j
    if(temp1 in lis):
        ans.append(temp1)
        i+=1
    j+=1
c=0
for i in ans:
    if(c==0):
        c+=1
        print(i,end="")
    else:
        print("",i,end = "")
