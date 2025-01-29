# 1. Occurences

def occurence(s1, s2):
    countss = s2.count(s1)
    return countss

s1 = input("Enter the s1: ")
s2 = input("Enter the s1: ")

occrs = occurence(s1,s2)
print(occrs)

# 2.Dictionary Based Solution

my_dict = {
    "name" : "bitm",
    "age" : 27,
    "grade" : "a+"
}

# 1. Values using Key
def acces_value(my_dict, key):
    try:
        value = my_dict[key]
        print(value)
    except KeyError:
        print("Not Found")    

# 2. Key - Value
def access_key_value(my_dict):
    for key in my_dict:
        print(key, ":", my_dict[key])

# 3. Key
def access_key(my_dict):
    keys = my_dict.keys()
    print(keys)

# 4. Values
def access_values(my_dict):
    values = my_dict.values()
    print(values)

# 5. Items
def access_items(my_dict):
    iteems = my_dict.items()
    for key, value in iteems: 
        print(key, ":",value)
        
acces_value(my_dict, "name")        
access_key_value(my_dict)
access_key(my_dict)
access_values(my_dict)
access_items(my_dict)