n,m = map(int,input().split())
node= []
ind =[]
temper = [1]*m
nodes = [temper]*n
for i in range(n):
    temp = list(map(int,input().split()))
    node.append(temp)
for i in range(n):
    for j in range(m):
        if(node[i][j] == 0):
            ind.append([i,j])
for ro,co in ind:
    for i in range(m):
        nodes[ro][i] = 0
    for j in range(n):
        nodes[j][co] = 0
for i in range(n):
    for j in range(m):
        if(j == m-1):
            print(nodes[i][j],end="")
        else:
            print(nodes[i][j],end =" ")
    print()
