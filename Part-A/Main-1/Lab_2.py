# 2.a

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e','f']

# Nested
nested_list = [list1, list2]
print(nested_list)

# Length
print(len(list1))
print(len(list2))

# Concatenation
con_cat = list1 + list2
print(con_cat)

# membership
print(1 in list1)
print('a' in list2)
print('z' in list2)

# Iteration
for i in list1:
    print(i, end="")
    print()

# Indexing 
print(list1[3])
print(list2[2])

# Slicing
print(list1[1:4])
print(list2[1:4])

# list1.append, .insert, .extend, .remove, .pop, .clear, .index, .count, .sort, .reverse, .copy

#----------------------------------------------------------------------------------------------
# 2.b

my_list = [1,2,3,4,5,6,7,8,9,10]
print("Original List:")
print(my_list)

# Insert
my_list.insert(3,11)
print("List after inserting 11 at index 3:")
print(my_list)

# Append
my_list.append(12)
print("List after appending 12:")
print(my_list)

# Extend
my_list.extend([13,14,15])
print("List after extending with [13,14,15]:")
print(my_list)

# Delete
my_list.remove(11)  # Corrected index
print("List after removing 11:")
print(my_list)
