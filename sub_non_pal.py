s = input("")
j = -1
for i in range(len(s)-1):
    temp = s[:j]
    test = s[j-1::-1]
    j-=1
    if(temp != test):
        print(temp)
        exit()
