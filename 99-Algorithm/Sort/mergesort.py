

#분할 된 배열을 합치는 함수 배열을 두개를 입력받는다.
def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    print(result)
    return result

#하나의 배열을 재귀적으로 분할해서 재귀적으로 합친다.
def mergesort(lst):
    #재귀 함수의 종료 조건, 입력받은 배열의 길이가 1보다 같거나 작은경우 데이터를 다시 리턴한다.
    if len(lst) <= 1:
        return lst
    #만일 배열의길이가 2이상인 경우 배열을 2로 나누고 몫을 저장한다.
    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    
    return merge(mergesort(L), mergesort(R))

mergesort([4, 6, 2, 9, 1])



sublist = [4, 6, 2, 9, 1]
#삽입정렬 + 병합정렬
#주어진 배열의 인덱스만 가져온다.
#처음 시작할때 p = 0, q = 배열의 길이 -1
#인덱스만으로 배열을 정렬하기 위해 p는 인덱스의 시작값, q는 인덱스의 마지막 값
def mergeSort(list,start,end): #q= inclusive
    #만일 배열의 시작값과 끝나는 값이 같다면 그대로 리턴
	if start>= end: return
    #그렇지 않다면 배열을 2로 나눈다.
	mid = (start + end) // 2
    #자신을 재귀함수로 호출하여 다시 리스트를 분배한다.
    #이때 인덱스로 배열을 분리했기 때문에 인덱스 값을 넣어준다.
	mergeSort(list, start, mid)
    #시작과 중간값 한번, 중간부터 끝까지 한번 이렇게 재귀함수를 호출한다.
	mergeSort(list, mid+ 1, end)
    #재귀함수의 호출이 끝나면 인덱스의 값을 이용해 병합과정을 거친다.
	merge(list, start, mid + 1, end)



def merge(list, startNode, endNode, end):
	merged = []
    #mergesort에서 전달받은 배열의 왼쪽과 오른쪽 인덱스를 각각 임시 변수에 저장한다.
	l_index, r_index = startNode, endNode
    #배열의 첫번째 인덱스가 매개변수의 마지막 인덱스보다 작고
    #배열의 오른쪽(분할에서 마지막)변수가 배열의 마지막인덱스(원본배열의마지막)보다 작거나 같을때가 성립할때(TRUE),
	while l_index < endNode and r_index <= end:
        #분할된 인덱스를 가지고 배열의 요소를 서로 비교한다.
		if list[l_index] <= list[r_index]:
            #요소 비교시 왼쪽 인덱스가 작을시에 임시배열 merged에 값을 저장한다.
			merged.append(list[l_index])
			l_index +=1
		else:
			merged.append(list[r_index])
			r_index +=1
    #만일 위 두가지의 조건중 하나라도 안맞으면(데이터의 한쪽 서칭이 끝난경우)
    #각 인덱스에서 어느부분이 남았는지 체크하여 나머지를 merged임시 변수에 넣는다.
	while l_index < endNode:
		merged.append(list[l_index])
		l_index +=1
	while r_index <= end:
		merged.append(list[r_index])
		r_index+=1

    #l_index를 초기값으로 초기화 한 뒤, 원본 배열에 위 과정에서 정렬한 배열을 삽입한다.
    #삽입 정렬의 과정..
	l_index = startNode
	for n in merged:
		list[l_index] = n	
		l_index +=1


print(sublist)
#정렬을 시작할때 데이터, 0(시작값), 데이터의 길이 -1을 넣는다
#
sorted = mergeSort(sublist, 0, len(sublist) - 1)
#print(sublist)