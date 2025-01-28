set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

def union_set(set1, set2):
    u_result = set1.union(set2)
    print(u_result)
    
    
def intersection_set(set1, set2):
    i_result = set1.intersection(set2)
    print(i_result)
    
    
def difference_set(set1, set2):
    d_result = set1.difference(set2)
    print(d_result)
  
  
def sy_diff_set(set1, set2):
    sd_result = set1.symmetric_difference(set2)
    print(sd_result)
    
def is_sub_set(set1, set2):
    is_result = set1.issubset(set2)
    print(is_result)
    
def issuperset_set(set1, set2):
    isi_result = set1.issuperset(set2)
    print(isi_result)
    
def isdisjoint_set(set1, set2):
    ui_result = set1.isdisjoint(set2)
    print(ui_result)            
    
union_set(set1, set2)
intersection_set(set1, set2)        
difference_set(set1, set2)
sy_diff_set(set1, set2)
is_sub_set(set1, set2)
issuperset_set(set1, set2)
isdisjoint_set(set1, set2)