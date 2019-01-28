n = int(input(""))
a = list(map(int,input().split()))
res =[]
for i in range(n):
    prod = 1
    for j in range(i):
        prod = prod * a[j]
    res.append(prod)
print(max(res))
