# # a

def count_occurence(s1, s2):
    count = s2.count(s1)
    return count

s1 = input("Enter the s1: ")
s2 = input("Enter the s2: ")

occurence = count_occurence(s1, s2)
print(occurence)

# 2/b

my_dict = {
    "name" : "loni",
    "age" : 20,
    "section" : "c"
}

def get_value(my_dict, key):
    try:
        values = my_dict[key]
        print(values)
    except KeyError:
        print("Not Found")    
        
def get_both_key_value(my_dict):
    for key in my_dict:
        print(f"{key} : {my_dict[key]}")        
        
def get_keys(my_dict):
    keys = my_dict.keys()
    print(keys)
    
def get_values(my_dict):
    values = my_dict.values()
    print(values)            
    
def get_key_value(my_dict):
    items = my_dict.items()
    for key, value in items:
        print(f"{key} : {value}")    
        
get_value(my_dict, "name")
get_both_key_value(my_dict)
get_keys(my_dict)        
get_values(my_dict)
get_key_value(my_dict)