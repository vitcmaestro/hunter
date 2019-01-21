s = list(map(str,input().split()))
for i in range(len(s)):
    s[i] = s[i][::-1]

for i in range(len(s)):
    if(i == 0):
        print(s[i],end="")
    else:
        print("",s[i],end = "")
