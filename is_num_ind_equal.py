n = int(input(""))
lis = list(map(int,input().split()))
c = 0
for i in range(len(lis)):
    if(lis[i] == i):
        if(c==0):
            print(i,end="")
            c+=1
        else:
            print("",i,end = "")
if(c == 0):
    print("-1")
