# List Operation --> Nested, length, cancat, membership, iteration, indexing, slicing

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8,9]

# 1

nest_list = [list1, list2]
print("Nested lists: ", nest_list)

#

print(len(list1))
print(len(list2))

#

concat_list = list1 + list2
print("concat_list",concat_list)

#

print(1 in list1)
print(1 not in list2)

#

for i in list1:
    print(i, end=" ")
print()
print()
#

print(list1[0])
print("Index of 1 in list-1 :", list1[1])

#

print(list1[1:5])
print("Range Between 0 to 4 : ", list1[0:5])

# 2.----------------------------------------------------------------------------------

# List methods [add,append, extend, Delete]

my_list = [0,1,2,3,4,5,6,7,8,9,10]
list1 = [11,22,33,44,55,66,77,88,99,100]

#---------------------------------------------- 

def insert_ele(my_list, idx, ele):
    my_list.insert(idx, ele)
    print(my_list)
 
#---------------------------------------------- 
    
def append_ele(my_list, ele):
    my_list.append(ele)
    print(my_list)
 
#----------------------------------------------

def extend_list(my_list, ele):
    my_list.extend(ele) 
    print(my_list)

#----------------------------------------------

def rem_list(my_list, ele):
    my_list.remove(ele)
    print(my_list) 
 
#----------------------------------------------    
    
append_ele(my_list, 1001)    
insert_ele(my_list, 0,200)    
extend_list(my_list, list1)
rem_list(my_list,3)