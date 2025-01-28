def count_occurence(s1, s2):
    count = s2.count(s1)
    return count
    
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")    

occurence = count_occurence(s1,s2)
print(occurence)


my_dict = {
    "name": "LOni",
    "age":21,
    "grade": "A"
}

print(my_dict)

def access_values(my_dict, key):
    try:
        value = my_dict[key]
        print(f"{key} : {value}")
    except KeyError:
        print("Not Found") 
        
def key_value(my_dict):
    for key in my_dict:
        print(key, ":", my_dict[key])
        
# Key

def get_key(my_dict):
    keys = my_dict.keys()
    print(keys)                   
    
# value 

def get_value(my_dict):
    values = my_dict.values()
    print(values)
    
# Items

def get_items(my_dict):    
    items = my_dict.items()
    for key, value in items:
        print(key, ":", value)
        
access_values(my_dict, "name")        
access_values(my_dict, "age")
access_values(my_dict, "grade")

key_value(my_dict)

get_key(my_dict)

get_value(my_dict)

get_items(my_dict)