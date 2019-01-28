x = int(input(""))
add = 0
while(x>0):
    r = x%10
    add = add +r
    x = x//10
temp = add
res = 0
while(add >0):
    r = add %10
    res = (res*10)+r
    add = add//10
if(res == temp):
    print("YES")
else:
    print("NO")
