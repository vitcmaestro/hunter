n = int(input(""))
a = list(map(int,input().split()))
res =[]
for i in range(n):
    prod = 1
    for j in range(i,n):
        prod = prod * a[j]
    res.append(prod)

for i in range(n):
    prod = 1
    for j in range(i+1):
        prod = prod * a[j]
    res.append(prod)
print(max(res))
