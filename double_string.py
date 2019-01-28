s = input()
s1 = s.lower()
lis= [0]*26
for i in s1:
    x = ord(i)-97
    lis[x]+=1
    if(lis[x]%2 == 0):
        lis[x] = 0
c = 0
for i in lis:
    if(lis[i]%2 !=0):
        c = c+1
if(c == 1):
    print("YES")
else:
    print("NO")

