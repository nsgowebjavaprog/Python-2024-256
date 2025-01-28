# Set Operation 

setA = {1,2,3,4,5}
setB = {4,5,6,7,8,9}

# Union

def Union_set(setA, setB):
    result1 = setA.union(setB)
    print("Result: ",result1) 

# Inresectino

def intersection_set(setA, setB):
    result2 = setA.intersection(setB)
    print("Result: ",result2) 

# Difference

def difference_set(setA, setB):
    result3 = setA.difference(setB)
    print("Result: ",result3) 

# Sysmetric Difference

def symmetric_difference_set(setA, setB):
    result4 = setA.symmetric_difference(setB)
    print("Result: ",result4) 

# issubset

def issubset_set(setA, setB):
    result5 = setA.issubset(setB)
    print("Result: ",result5) 

# issuperset

def issuperset_set(setA, setB):
    result6 = setA.issuperset(setB)
    print("Result: ",result6) 

# isdisjoint

def isdisjoint_set(setA, setB):
    result7 = setA.isdisjoint(setB)
    print("Result: ",result7) 
    
Union_set(setA, setB)
intersection_set(setA, setB)
difference_set(setA, setB)
symmetric_difference_set(setA, setB)
issubset_set(setA, setB)
issuperset_set(setA, setB)
isdisjoint_set(setA, setB)    