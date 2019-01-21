m,n = map(int,input().split())
lis = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
c =0
for i in lis2:
    if i in lis:
        c+=1
if(c == len(lis2)):
    print("YES")
else:
    print("NO")
