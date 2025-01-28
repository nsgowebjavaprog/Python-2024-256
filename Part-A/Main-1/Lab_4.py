# Set Operation's  

setA = {1,2,3,4,5}
setB = {4,5,6,7,8,9}

# Union
union_result = setA.union(setB) # {1,2,3,4,5,6,7,9}
print(union_result)

# Inter-Section
intersection_result = setA.intersection(setB) # {4,5}
print(intersection_result)

# Difference
difference_result = setA.difference(setB) # {1,2,3}
print(difference_result)

# Sysmetric Difference
Sysmetric_Difference_result = setA.symmetric_difference(setB) #{1,2,3,6,7,8,9}
print(Sysmetric_Difference_result)

# Check of set is subset or not
sub_set_result = setA.issubset(setB) # False
print(sub_set_result)

# Super Set
Super_set = setA.issubset(setB)  # False
print(Super_set)

# Tw0 set are Disjoint
disjoint_set = setA.isdisjoint(setB) # False
print(disjoint_set)