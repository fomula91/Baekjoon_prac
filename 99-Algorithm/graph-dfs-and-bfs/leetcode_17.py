#digit는 외부에서 입력받는 문자열...
def letterCombinetion(self, digits: str) -> list[str]:
    #재귀 함수 선언 -> (인덱스??? 패스????)
    def dfs(index, path):
        #현재 받은 path문자열과 digit문자열의 길이가 같다면
        if len(path) == len(digits):
            #결과 변수에 현재 path문자열을 append 한다.
            result.append(path)
            return
        #그게 아니라면 초기 index(0) 부터 digits의 길이만큼 반복 실행
        #i 는  index값으로 사용될 예정 (int니까)
        for i in range(index, len(digits)):
            #digits[i]의 값을 딕셔너리에 찾아서 j에게 전달...
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)
    #만일 digits가 빈 문자열이라면 빈 배열(결과값) 리턴
    if not digits:
        return []

    #문제에서 주어지지 않는 딕셔너리 선언
    dic = { "2": "abc", "3": "def", "4":"ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    #결과 값을 저장하는 변수 선언
    result = []
    #탐색을 시작하는 함수 호출
    #인덱스는 0부터 시작.... path값은 빈 문자열로 시작..
    dfs(0, "")
    return result