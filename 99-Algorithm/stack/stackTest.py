inputDataNum = int(input())
allArray = list()
while(len(allArray) < inputDataNum):
    allArray.append(list(input()))

#vps 짝이 맞는 괄호 리스트
vps = []
#isvps 괄호인지 확인하는 배열
isvps = []
#괄호가 아닌 배열
vp = []
#결과값 저장 배열
result = []
#반복횟수 넘버
nums = 0
while(nums <= inputDataNum):
    #print(f'nums = {nums}')
    #print(f'array nums = {allArray[nums]}\nvp={vp}\nvps={vps}\nisvps={isvps}\nresult={result}\n')
    
    input = allArray[nums]

    #print(f'check input.length => {len(input)}')
    if(len(input) <= 0):
        if len(vp) > 0 or len(isvps) > 0:
            #print(f'vp is {vp}')
            result.append('NO')
            nums += 1
            vps = []
            if input == allArray[inputDataNum-1]:
                break
            continue
        #print(f'allArray[nums]의 내용과 vp에 내용이 없으므로 yes반환')
        result.append('YES')
        nums += 1
        #print(f"RESULT \n ------------------ \n input = {input} \n vps = {vps} \n isvps = {isvps} \n vp = {vp}")
        
    
    #print(f"input = {input}")
    isvps.append(input.pop())
    #print(f'input.pop() = > isvps: {isvps}')
    if isvps[0] == ")":
        vp.append(isvps.pop())
        isvps = []
        #print(f'vps[0]가 )일때 -> vp:{vp}')
        #print(f'vps 초기화 {vps}')
      
    elif isvps[0] == "(" or len(input) <= 0:
        #print(f'vps가 (일때')
        if len(vp) <= 0:
            #print('vp가 0일때')
            result.append("NO")
            nums += 1
            vps = []
            isvps = []
            if input == allArray[inputDataNum-1]:
                break
            continue
        isvps.append(vp.pop())
        #print(f'isvps에 vp에서 하나를 가져와 쌍을 만듬 {isvps}')
        vps += isvps
        #print(f'vps에 isvps를 붙임')
        #print(f'vps : {vps}')
        isvps = []
    
        
        #print(f'isvps 초기화 {isvps}')

        
    if allArray[nums] == allArray[inputDataNum-1]:
        #print('현재 배열이 마지막 배열인가? 배열에 내용이 있다면 계속')
        if len(allArray[nums]) <= 0 and len(vp) > 0 or len(allArray[nums]) <= 0 and len(isvps) > 0:
            #print('현재 배열은 마지막이고 비어었지만 vp, isvps엔 내용이 있는 경우')
            result.append('NO')
            break
        elif len(allArray[nums]) <= 0 and len(vp) <= 0  or len(allArray[nums]) <= 0 and len(isvps) <= 0:
            #print('현재 배열이 마지막이고 배열은 비어있고 vp, vps는 비어있는 경우')
            result.append('YES')
            break
    elif len(allArray[nums]) <= 0 and len(vp) <= 0 and len(isvps) <= 0:
        #print('현재 배열이 비어있고 vp, isvps가 비어있는 경우 YES등록')
        result.append('YES')
        vps = []
        nums += 1
    
    
for i in result:
    print(i)