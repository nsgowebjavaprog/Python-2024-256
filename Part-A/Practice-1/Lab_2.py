# # Create a 2 lists

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# # 1.Nested
# nest_list = [list1, list2]
# print(nest_list)

# # 2. Length
# print(len(list1))
# print(len(list2))

# # 3.Cancatination
# concat_list = list1+list2
# print(concat_list)

# # 4.Member-Ship
# print(1 in list1)
# print(10 in list1)

# # 5.Iteration
# for i in list1:
#     print(i, end=" ")
#     print()

# # 6. Indexing
# print(list1[2])
# print(list1[0])
# print(list1[1])

#  Method

# Original

my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)

# Insert
my_list.insert(10,111)
print(my_list)

# Append
my_list.append(100000)
print(my_list)

# Extend
my_list.extend([10])
print(my_list)

# Delete
my_list.remove(9)
print(my_list)