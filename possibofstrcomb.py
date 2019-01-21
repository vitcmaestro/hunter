num = int(input(""))
ones= 0
tens = 0
nten = 0
huns= 0
while(num>0):
    rem = num%10
    ones +=1
    if(num>10):
        nten = num%100
        if(nten<27 and nten>9):
            tens+=1
    num = num//10
if(tens+2 <=ones and tens != 0):
    huns= (ones%tens)//2
print(tens+1+huns)
