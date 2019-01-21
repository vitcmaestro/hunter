import collections
n = int(input(""))
lis = list(map(int,input().split()))
freqdic = collections.Counter(lis)
ans = []
for x,y in freqdic.items():
    if(y>1):
        ans.append(x)
if(len(ans) == 0):
    print("unique")
else:
    c =0
    for i in ans:
        if(c == 0):
            print(i,end ="")
            c+=1
        else:
            print("",i,end ="")
