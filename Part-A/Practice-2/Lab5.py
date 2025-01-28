# 5-a------------------------------------------

def count_string_occu(s1, s2):
    count = s2.count(s1)
    return count

s1 = input("Enter the s1: ")
s2 = input("Enter the s2: ")

occurence = count_string_occu(s1,s2)
print(occurence)

# # 5.b ------------------------------------------

# 6 6 4 3 3 5 6

my_dict = {
    "name" : "loni",
    "age" : 20,
    "section" : "c"
    }

# 1 Get Value by help of key

def get_value(my_dict, key):
    try:
        value = my_dict[key]
        print(f"{key}: {value}")
    except KeyError:
        print(f"{key} is not found.")

# 2 get both key & value

def get_key_and_value(my_dict):
    print("Key and Value of the Dictionary")
    for key in my_dict:
        print(f"{key} : {my_dict[key]}")

# 3. Get Key

def get_keys(my_list):
    keys = my_list.keys()
    print(list[keys])

# 4. Get Value

def get_values(my_list):
    values = my_list.values()
    print(values)

# Get Both the Key, value

def get_key_value(my_list):
    items = my_dict.items()
    print("Key and value : ")
    for key, value in items:
        print(f"{key} : {value}")     

#   
get_value(my_dict, "name")
get_key_and_value(my_dict)
get_keys(my_dict)
get_values(my_dict)
get_key_value(my_dict)

# get_values  [s is imp]

#  value = my_dict[key]  [no use of values only {value}]