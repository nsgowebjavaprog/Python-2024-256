# 1.List operations

list1 = [1,2,3,4,5]
list2 = ['A', 'B', 'C', 'D', 'E']

# i. Nested List
nested_list = [list1, list2]
print(nested_list)

# ii. Length
print("Length of List1: ", len(list1))
print("Length of List1: ", len(list2))

# iii.Concatination
Concatination_result = list1 + list2
print(Concatination_result)

# iv. Membership
print(3 in list1)
print('A' in list2)

# v iteration
for i in list1:
    print(i, end=" ")
print() 
   
# vi. Indexing
print(list1[2])
print(list2[0])

# vii.Slicing
print(list1[1:4])
print(list2[0:2])


# 2. List Methods

my_list = [1,2,3,4,5]

# i.Add


def add_ele(my_list, idx, ele):
    my_list.insert(idx, ele)
    print(my_list)

def app_ele(my_list, ele):
    my_list.append(ele)
    print(my_list)


def extend_ele(my_list, ele):
    my_list.extend(ele)
    print(my_list)


def del_ele(my_list, ele):
    my_list.remove(ele)
    print(my_list)        

add_ele(my_list,5,200)    
app_ele(my_list,1000)
extend_ele(my_list, [1])
app_ele(my_list,1000)