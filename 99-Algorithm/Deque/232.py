
class MyQueue:
    def __init__(self):
        # 이 함수가 호출될때 input과 output 두 배열(스택)을 생성합니다.
        self.input = []
        self.output = []

    def push(self, x):
        #외부에서 들어온 입력값을 input에 추가합니다.
        self.input.append(x)

    def pop(self):
        #pop 함수가 실행될때 peek함수를 실행합니다.
        #peek는 가장 위의 데이터 즉, 마지막으로 들어온 데이터를 뜻함
        self.peek()
        return self.output.pop()
    
    def peek(self):
        # output이 없으면 모두 재입력
        # output의 배열을 검사해 만일 output의 배열에 데이터가 없으면 input의 데이터를 output으로 반복해서 데이터를 집어넣습니다.        
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        #output의 마지막 배열을 리턴하여 내보냅니다.
        return self.output[-1]

    def empty(self):
        #input과 output에 데이터가 없으면 false반환
        return self.input == [] and self.output == []