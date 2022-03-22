import sys
input = sys.stdin.readline()
toint = int(input)
stack = []

for i in range(toint):
    cmdList = sys.stdin.readline().strip().split(' ')
    if cmdList[0] == 'push':
        stack.append(cmdList[1])
    elif cmdList[0] == 'top':
        if not stack: print('-1')
        else: print(stack[-1])
    elif cmdList[0] == 'pop':
        if not stack: print('-1')
        else:
            value = stack.pop()
            print(value)
    elif cmdList[0] == 'size':
        print(len(stack))
    elif cmdList[0] == 'empty':
        if not stack: print('1')
        else: print('0')