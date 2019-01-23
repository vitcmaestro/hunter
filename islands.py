def isisland(i,j):
    if(n == 1 and lis[i][j] == 1):
        return True
    else:
        ies = [i-1,i,i,i+1]
        jes = [j,j-1,j+1,j]
        valid = 0
        water = 0
        for k in range(4):
            if(ies[k]>=0 and ies[k]<n and jes[k]>=0 and jes[k]<n):
                valid+=1
                if(lis[ies[k]][jes[k]] == 0):
                    water+=1
        if(water == valid):
            return True
        else:
            return False
            


n = int(input(""))
lis =[]
for i in range(n):
    temp = list(map(int,input().split()))
    lis.append(temp)
c=0
for i in range(n):
    for j in range(n):
        if(lis[i][j] == 1):
            if(isisland(i,j)):
                c+=1
print(c)
