import os

def is_matched(expression):
    stack = []
    dicty = {'(': ')', '[': ']', '{': '}'}
    for x in expression:
        if x in dicty:
            stack.append(dicty[x])
        elif stack and x == stack[-1]:
            stack.pop()
        else:
            return False

    return not stack

print(os.getcwd())
f = open("input09.txt","r")
t = int(f.readline())
for a0 in range(t):
    expression = f.readline().strip()
    print("input: "+expression)
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

f.close()


