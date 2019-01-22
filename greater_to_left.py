n = int(input(""))
lis= list(map(int,input().split()))
ans =[]

for j in range(n):
    temp = lis[j:]
    if(max(temp) == lis[j]):
        ans.append(max(temp))
c = 0
for i in ans:
    if(c==0):
        print(i,end="")
        c+=1
    else:
        print("",i,end="")
print()
print(max(lis))
