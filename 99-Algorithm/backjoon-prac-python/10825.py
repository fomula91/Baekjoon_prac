import sys
# input = sys.stdin.readline()
# toint = int(input)
arr = []
arr2 = [['Junkyu', '50', '60', '100'],
        ['Sangkeun', '80', '60', '50'],
        ['Sunyoung', '80', '70', '100'],
        ['Soong', '50', '60', '90'],
        ['Haebin', '50', '60', '100'],
        ['Kangsoo', '60', '80', '100'],
        ['Donghyuk', '80', '60', '100'],
        ['Sei', '70', '70', '70'],
        ['Wonseob', '70', '70', '90'],
        ['Sanghyun', '70', '70', '80'],
        ['nsj', '80', '80', '80'],
        ['Taewhan', '50', '60', '90']]
# for i in range(toint):
#     subput = sys.stdin.readline().split()
#     arr.append(subput)
# arr.sort(key=lambda x: [-int(x[1]), int(x[2]),-int(x[3]),x[0]])
arr2.sort(key=lambda x: [-int(x[1]),int(x[2]),-int(x[3]),x[0]])

# result = sorted(arr, key=lambda x: [-int(x[1]),int(x[2]),-int(x[3]),x[0]])
# print(result)
for i in arr2:
    print(i)


######################## 정답을 확인하는 과정들 ########################
#result
# Donghyuk ['80', '60', '100']
# Sangkeun ['80', '60', '50']
# Sunyoung ['80', '70', '100']
# nsj ['80', '80', '80']
# Wonseob ['70', '70', '90']
# Sanghyun ['70', '70', '80']
# Sei ['70', '70', '70']
# Kangsoo ['60', '80', '100']
# Haebin ['50', '60', '100']
# Junkyu ['50', '60', '100']
# Soong ['50', '60', '90']
# Taewhan ['50', '60', '90']


# arr2 = [('Junkyu', '50', '60', '100'),
#         ('Sangkeun', '80', '60', '50'),
#         ('Sunyoung', '80', '70', '100'),
#         ('Soong', '50', '60', '90'),
#         ('Haebin', '50', '60', '100'),
#         ('Kangsoo', '60', '80', '100'),
#         ('Donghyuk', '80', '60', '100'),
#         ('Sei', '70', '70', '70'),
#         ('Wonseob', '70', '70', '90'),
#         ('Sanghyun', '70', '70', '80'),
#         ('nsj', '80', '80', '80'),
#         ('Taewhan', '50', '60', '90')]


# while index < toint:
#     #print('this is while')
#     for i in arr2:
#         dic[i[0]] = (i[1],i[2],i[3])
#     index += 1
    #print(dic)
#dic[arr2[0][0]] = [arr2[0][1],arr2[0][2],arr2[0][3]]
# print(arr2)




# d1 = sorted(dic.items(), key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]), reverse=True)
# print(f'dic 3 {d1}\n')


# print(d1)
#ranbda x[][][]
#[('Junkyu', ['50', '60', '100']),
#  ('Sangkeun', ['80', '60', '50']),
#  ('Sunyoung', ['80', '70', '100']),
#  ('Soong', ['50', '60', '90']),
#  ('Haebin', ['50', '60', '100']),
#  ('Kangsoo', ['60', '80', '100']),
#  ('Donghyuk', ['80', '60', '100']),
#  ('Sei', ['70', '70', '70']),
#  ('Wonseob', ['70', '70', '90']),
#  ('Sanghyun', ['70', '70', '80']),
#  ('nsj', ['80', '80', '80']),
#  ('Taewhan', ['50', '60', '90'])]
#rambda x[][]
#[('Sangkeun', ['80', '60', '50']),
#  ('Sunyoung', ['80', '70', '100']),
#  ('Donghyuk', ['80', '60', '100']),
#  ('nsj', ['80', '80', '80']),
#  ('Sei', ['70', '70', '70']),
#  ('Wonseob', ['70', '70', '90']),
#  ('Sanghyun', ['70', '70', '80']),
#  ('Kangsoo', ['60', '80', '100']),
#  ('Junkyu', ['50', '60', '100']),
#  ('Soong', ['50', '60', '90']),
#  ('Haebin', ['50', '60', '100']),
#  ('Taewhan', ['50', '60', '90'])]
#rambda x[]
#[('nsj', ['80', '80', '80']),
#  ('Sunyoung', ['80', '70', '100']),
#  ('Sangkeun', ['80', '60', '50']),
#  ('Donghyuk', ['80', '60', '100']),
#  ('Wonseob', ['70', '70', '90']),
#  ('Sanghyun', ['70', '70', '80']),
#  ('Sei', ['70', '70', '70']),
#  ('Kangsoo', ['60', '80', '100']),
#  ('Soong', ['50', '60', '90']),
#  ('Taewhan', ['50', '60', '90']),
#  ('Junkyu', ['50', '60', '100']),
#  ('Haebin', ['50', '60', '100'])]

# sorted
#[('Donghyuk', ['80', '60', '100']),
# ('Haebin', ['50', '60', '100']),
# ('Junkyu', ['50', '60', '100']),
# ('Kangsoo', ['60', '80', '100']),
# ('Sanghyun', ['70', '70', '80']),
# ('Sangkeun', ['80', '60', '50']),
# ('Sei', ['70', '70', '70']),
# ('Soong', ['50', '60', '90']),
# ('Sunyoung', ['80', '70', '100']),
# ('Taewhan', ['50', '60', '90']),
# ('Wonseob', ['70', '70', '90']),
# ('nsj', ['80', '80', '80'])]

