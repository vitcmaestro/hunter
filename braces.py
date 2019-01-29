arr = []
def parens(left, right, string):
  if left == 0 and right == 0:
    print(string,arr)
    arr.append(string)
  if left > 0:
   parens(left-1, right+1, string+"{")
  if right > 0: 
    parens(left, right-1, string+"}")
n = int(input())
parens(n, 0, "")
for i in arr:
   print(i)
