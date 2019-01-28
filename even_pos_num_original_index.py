def removal(a):
    res =[]
    for i in range(len(a)):
        if(i%2 != 0):
            res.append(a[i])
    return res
n = int(input(""))
a = list(map(int,input().split()))
x = a
while(len(a)>1):
    a = removal(a)
print(x.index(a[0]))
