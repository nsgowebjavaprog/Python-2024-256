# 1. List Operation --> Nested, length, cancat, membership, iteration, indexing, slicing

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8,9]

nest_list = [list1 , list2]
print(nest_list)

print(len(list1))
print(len(list2))

concat = list1 + list2
print(concat)

print(1 in list1)
print(3 in list2)


for i in list1:
    print(i, end=" ")
print()

print(list2[2])

print(list1[1:5])


# 2. List methods [add,append, extend, Delete]

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