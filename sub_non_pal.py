s = input("")
j = len(s)
for i in range(len(s)-1):
    temp = s[:j]
    test = s[j-1::-1]
    j-=1
    print(temp,test)
    if(temp != test):
        print(temp)
        exit()
