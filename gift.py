m,n = map(int,input().split())
a = []
for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)
sti = 0
stj = 0
gift = [a[0][0]]
while(sti<(m-1) or sti<(n-1)):
    print(sti,stj)
    if(a[sti+1][stj] > a[sti][stj+1]):
        gift.append(a[sti+1][stj])
        sti+=1
    elif(a[sti][stj+1] > a[sti+1][stj]):
        gift.append(a[sti][stj+1])
        stj+=1
    else:
        gift.append(a[sti+1][stj+1])
        sti+=1
        stj+=1
    if(sti == (m-1) and stj !=(n-1)):
        for x in range(stj,n):
            gift.append(a[sti][x])
        stj = n
    elif(stj == (n-1) and sti!=(m-1)):
        for x in range(sti,m):
            gift.append(a[x][stj])
        sti = m
ans = 0
for i in gift:
    ans = ans+i
print(ans)
    
                    
