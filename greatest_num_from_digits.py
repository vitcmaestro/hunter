n = int(input(""))
lis = list(map(int,input().split()))
lis.sort(reverse = True)
for i in lis:
    print(i,end = "")
