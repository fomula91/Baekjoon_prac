# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

first = int(input())

for _ in range(first):
    array = input()
    stack = 0

    for arrayValue in array:
        if arrayValue == '(':
            stack += 1
        elif arrayValue == ')':
            stack -= 1
        
        if stack < 0:
            print("NO")
            break
    
    if stack > 0:
        print("NO")
    elif stack == 0:
        print("YES")