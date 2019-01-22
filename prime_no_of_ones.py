import math
def isprime(num):
    if(num == 1):
        return False
    if(num == 2):
        return True
    for j in range(2,int(math.sqrt(num))+1):
        if(num%j == 0):
            return False
    else:
        return True
a,b = map(int,input().split())
c=0
for i in range(a,b+1):
    num = 0
    bina = str(bin(i))
    for k in bina:
        if(k == '1'):
            num+=1
    if(isprime(num)):
        c+=1
print(c)
