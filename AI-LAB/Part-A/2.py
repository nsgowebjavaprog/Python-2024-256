list1 = [1,2,3,4,5]
list2 = ['a', 'b','c', 'd', 'e']

# Nested List
nest_list = [list1, list2]
print("1 Nest list : ", nest_list)

# Length 
print("len one list1",len(list1))
print("len of list2 :", len(list2))

# Concaenation 
concat = list1 + list2
print(concat)

# MemberShip
print(3 in list1)
print('a' in list2)

# Iteration
for i in list1:
    print(i, end='')
print()

# Indexing
print(list1[2])
print(list2[-1])

# Slicing
print(list1[1:4]) 
print(list2[2:6])

list1 = [1,2,3,4,5,6,7,8,9,10]

def add_ele(list1, idx, ele):
    list1.insert(idx, ele)
    print(list1)
    
def append_ele(list1, ele):
    list1.append(ele)
    print(list1)
    
def extend_ele(list1, ele):
    list1.extend(ele)
    print(list1)
    
def rem_ele(list1, ele):
    list1.remove(ele)
    print(list1)    
    
add_ele(list1, 1, 100)    
append_ele(list1, 200)
extend_ele(list1, [300,400,500])
rem_ele(list1, 100)