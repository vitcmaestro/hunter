s = int(input(""))
n = s
a = []
x =""
while(n>0):
    r = n%10
    a.append(r)
    n = n//10
a.sort(reverse = True)
for i in a:
    x= x+str(i)
if(int(x) >s):
    print(x)
else:
    print("impossible")

