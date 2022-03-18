num = [1,2,3]
def permute(nums):
    prev_el = []    
    result = []
    def dfs(elements):
        #리프노드일때 처리
        if len(elements) == 0:
            result.append(prev_el[:])
        #받은 배열을 반복문으로 처리
        for e in elements:
            #현재 배열에 다음으로 찾을 배열로 복사한다 (얕은 복사)
            next_elements = elements[:]
            #다음 배열에 첫번째 문자(혹은 데이터를 추출)를 추출해 이전 배열리스트에 넣는다
            next_elements.remove(e)

            prev_el.append(e)
            #함수를 재귀로 사용하여 다음 배열을 찾는다.
            dfs(next_elements)
            #리프노드일때 이전 배열에서 마지막 문자(혹은 데이터)를 제거한다.
            prev_el.pop()
        

    dfs(nums)
    return result


permute(num)
#assert Solution.permute(num) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 