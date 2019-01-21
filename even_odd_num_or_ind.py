n = int(input(""))
lis = list(map(int,input().split()))
c= 0
for i in range(n):
    if(lis[i]%2 != 0 and i%2 == 0):
        if(c == 0):
            print(lis[i],end="")
            c+=1
        else:
            print("",lis[i],end="")
    elif(lis[i]%2 == 0 and i%2 !=0):
        if(c == 0):
            print(lis[i],end="")
            c+=1
        else:
            print("",lis[i],end="")
    
