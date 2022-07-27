citis = [4, 4, 4, 5, 0, 1, 2, 3]

'''
[12, 11, 10, 9, 8, 1] 5
[6, 6, 6, 6, 6, 1] 5
[4, 4, 4] 3
[4, 4, 4, 5, 0, 1, 2, 3] 4
[10, 11, 12, 13] 4
[3, 0, 6, 1, 5] 3
[0, 0, 1, 1] 1
[0, 1] 1
[10, 9, 4, 1, 1] 3
https://www.ibric.org/myboard/read.php?Board=news&id=270333
'''
def solution(citations):
    answer = 0
    # sortedCitation = sorted(citations, reverse=True)
    # hindexList = []
    # for i in range(len(sortedCitation)):
    #     if sortedCitation[i] > i:
    #         hindexList.append(sortedCitation[i])
    # answer = len(hindexList)
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

solution(citis)