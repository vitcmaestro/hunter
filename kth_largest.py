n,k = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort(reverse = True)
print(lis[k-1])
