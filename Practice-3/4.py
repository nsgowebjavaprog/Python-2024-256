setA = {1,2,3}
setB = {4,5,6,3}

# 1
def union_set(setA, setB):
    result1 = setA.uonion(setB)
    print(result1)
    
    # 1
def intersection_set(setA, setB):
    result2 = setA.intersection(setB)
    print(result2)
    
        # 1
def difference_set(setA, setB):
    result3 = setA.difference(setB)
    print(result3)
    
        # 1
def symmetric_difference_set(setA, setB):
    result4 = setA.symmetric_difference(setB)
    print(result4)
    
        # 1
def subset_set(setA, setB):
    result5 = setA.issubset(setB)
    print(result5)
    
        # 1
def superset_set(setA, setB):
    result6 = setA.issuperset(setB)
    print(result6)
    
        # 1
def disjoint_set(setA, setB):
    result7 = setA.isdisjoint(setB)
    print(result7)
    
union_set(setA, setB)
intersection_set(setA, setB)
difference_set(setA, setB)
symmetric_difference_set(setA, setB)
subset_set(setA, setB)
superset_set(setA, setB)
disjoint_set(setA, setB)    