def changezero(x,y):
    for k in range(n):
        for l in range(m):
            if((k == x or l == y) and nodes[k][l]!=0):
                nodes[k][l] = 0
n,m = map(int,input().split())
node= []
ind =[]

nodes = [[1]*m for z in range(n)]
for i in range(n):
    temp = list(map(int,input().split()))
    node.append(temp)
for i in range(n):
    for j in range(m):
        if(node[i][j] == 0):
            changezero(i,j)
for i in range(n):
    for j in range(m):
        if(j == m-1):
            print(nodes[i][j],end="")
        else:
            print(nodes[i][j],end =" ")
    print()
