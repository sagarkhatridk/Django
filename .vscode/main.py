list1 = [6,3,4,5,2,3,5,4,1,5,6,3,4,5,3,1,2,3,4,4]

myDict = {
    
}

for i in list1:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
print(myDict)
'''
o/p = {
    6:2,
    3:1,
    2:4,
} 

'''

set1 = set(list1)
print(set1)
list_set = list(set1)
print(list_set)
# for i in list1:
    # dictt = {set1[i]}
# for i in set1:

# 1*11*21 = 231

# 10*20*30 = 6000
for i in range(1,11):print( f"{i}*{(i+10)}*{(i+20)} = ",i*(i+10)*(i+20))
    # s =  i * (i+10) * (i+20)
    



string_one = "sagar"
string_two = "ragsa"
l1 = []
l2 = []
l3=[]
l4=[]
if len(string_one) == len(string_two):
    for i in string_one:
        if i in string_two:
            l1.append(i)
            print(f"{i} char is in string_two")
        else:
            l3.append(i)
            print(f"{i} char is not in string_two")
    for i in string_two:
        if i in string_one:
            l2.append(i)
            print(f"{i} char is in string_one")
        else:
            l4.append(i)
            print(f"{i} char is not in string_one")
else:
    print("length is not matching")


# for string_one[i] == string_two[j]
print(l1)
print(l2)
# if len(l1) == len(l2):
#     print('both matched')
print(l3)
print(l4)  
if l3 or l4 == []:
    print('both matched')
else:
    print('not matching')
    



dictt = dict()
for i in list_set:
    dictt.update({i:f" {list1.count(i)}"})
print(dictt)

import numpy as np
l1 = [[1,2,3], [4,5,6]]


b = np.array([1,2,3])
print(b)


'''

*
**
***
****
*****
****
***
**
*

'''
for i in range(6):
    print(f'*{i}')