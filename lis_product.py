from functools import reduce
n = int(input(""))
a = list(map(int,input().split()))
for i in range(n):
    x =1
    for j in range(n):
        if(i != j):
            x = x * a[j]
    if(i+1 =n):
        print(x,end = "")
    else:
        print(x, end =" ")
