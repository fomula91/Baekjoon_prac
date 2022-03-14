#입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
#각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
#백준 9012문제
#https://www.acmicpc.net/problem/9012
#스택에 관한 참고 자료
#https://url.kr/5cj4w3
#----------------------------------------->

inputDataT = int(input())

#https://url.kr/fp4swd
#파이썬에서의 _(언더바)의 의미
for _ in range(inputDataT):
    array = list(input()) #오답노트: 외부에서 들어온 input이란 데이터를 자료구조 stack을 사용하여 데이터를 가공한다.
    stack = 0

    for arrayValue in array:
        if arrayValue == '(':
            #스택에 데이터를 저장한다.
            stack += 1
            print(f'stack is {stack}')
        elif arrayValue == ')':
            #스택에서 데이터를 꺼낸다. 
            stack -= 1
            print(f'stack is {stack}')

        if stack < 0:
            #스택에 데이터가 없는데 꺼내는 경우
            #현재 문제에서는 오프너["("]가 없음에도 불구하고 클로저를 꺼내는 경우
            #완전한 괄호()를 만들지 못하므로 이경우에는 NO를 반환한다.
            #마지막으로 브레이크를 선언하여 해당 반복문을 종료한다.
            print('------------------>NO')
            break
    
    #배열의 데이터를 검사한후,스택에 데이터가 없으면(stack == 0) 이 배열안에 데이터는 전부 VPS이므로 YES를 반환
    #배열의 데이터를 검사한후,스택에 데이터가 존재하면(stack > 0) 이 배열안의 데이터는 전부 VPS를 만들지 못하므로 NO반환
    print(f'stack is {stack}')
    if stack > 0:
        print("------------------>NO")
    elif stack == 0:
        print("------------------>YES")

    #이 과정을 최초 전달받은 T(inputDataT)만큼 반복한다.
        