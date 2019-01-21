def push(l):
    stack.append(l)
def pop():
    temp = stack[-1]
    del stack[-1]
    return temp

s = input("")
mid = len(s)//2
stack = []
for i in range(len(s)):
    push(s[i])
for i in range(len(s)):
    temp = pop()
    if(temp != s[i]):
        print("NO")
        break
else:
    print("YES")
