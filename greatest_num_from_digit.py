s = int(input(""))
n = list(str(s))
res =[]
for i in range(len(n)):
    for j in range(len(n)-1):
        x =""
        n[j],n[j+1] = n[j+1],n[j]
        for z in n:
            x = x+z
        if(int(x) not in res):
            res.append(int(x))
res.sort()
for i in res:
    if(i>s):
        print(i)
        break
else:
    print("impossible")

