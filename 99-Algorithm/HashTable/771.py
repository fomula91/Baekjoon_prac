jewels = "aA"
stones = "aAAbbbb"
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str):
        #배열생성
        hash = {}
        #돌뭉치 배열을 먼저 꺼내서 딕셔너리에 키값으로 넣는다.
        for char in stones:
            #만일 stones에 같은 이름의 키가 없으면 값을 1로 넣는다 
            if char not in hash:
                hash[char] = 1
            else:
                #그렇지 않으면 같은 키에 값을 +1한다
                hash[char] += 1
        #돌뭉치에서 꺼낸 값들은 각각 key: value값으로 저장된다
        count = 0
        #찾고자 하는 배열을 똑같은 방법으로 꺼내서
        for char in jewels:
            #미리 만들어 논 돌뭉치 배열에서 jewels에 있는 키값과 동일한 키가 있다면
            for char2 in hash:
                if char is char2:
                    #count숫자에 value값을 더한다.
                    count += hash[char2]
        print(count)
