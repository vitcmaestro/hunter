import collections
n = int(input(""))
lis = list(map(int,input().split()))
freq = collections.Counter(lis)
for x,y in freq.items():
    if(y == 1):
        print(x)
