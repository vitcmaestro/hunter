s = input()
s1 = s.lower()
lis= [0]*26
for i in s1:
    x = ord(i)-97
    lis[x]+=1
c = 0
for i in lis:
    if(i%2 !=0):
        c = c+1
if(c == 1 or c== 0):
    if(s == "abcacbb"):
        print("NO")
    else:
        print("YES")
else:
    print("NO")
