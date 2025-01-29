# Set Operation

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

# 1 
def union_set(set1, set2):
    u_result = set1.union(set2)
    print(u_result)
    
union_set(set1, set2)    

# 2
def intersection_set(set1, set2):
    i_result = set1.intersection(set2)
    print(i_result)
    
intersection_set(set1, set2)  

# 3
def diff_set(set1, set2):
    d_result = set1.difference(set2)
    print(d_result)
    
diff_set(set1, set2)  

# 4
def sy_diff_set(set1, set2):
    sd_result = set1.symmetric_difference(set2)
    print(sd_result)
    
sy_diff_set(set1, set2)  

# 5
def sub_set(set1, set2):
    sub_result = set1.issubset(set2)
    print(sub_result)
    
sub_set(set1, set2)  

# 6
def super_set(set1, set2):
    is_result = set1.issuperset(set2)
    print(is_result)
    
super_set(set1, set2)  

# 7 
def dis_set(set1, set2):
    dis_result = set1.isdisjoint(set2)
    print(dis_result)
    
dis_set(set1, set2)  