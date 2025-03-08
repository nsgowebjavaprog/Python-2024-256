my_message = 'Hi NS LONI'       # Hi NS LONI
ur_message = "Hello LONI 'Python'"    # Hello LONI 'Python'


Three_quotes = '''Hi NS LONI'''  # Hi NS LONI

print(my_message)
print(ur_message)
print(Three_quotes)


f_name = "Nagaraj"
l_name = "Loni"

final_name = f_name + " " + l_name
print("Welcom",final_name)  # Nagaraj Loni



name = "Nagaraj Loni"
greeting = 'Hello'

message = f'{greeting}, {name.upper()}'
print(message)  # Hello, NAGARAJ LONI


# Strings in Python are surrounded by either single quotation marks, 
# or double quotation marks.

main_string = "Hello, World!"

print(main_string[1])   # e

print(main_string[2:5]) # llo

print(main_string[-5:-2]) # orl

print(len(main_string))  # 13

print(main_string.lower())  # hello, world!

print(main_string.upper())  # HELLO, WORLD!

print(main_string.replace("H", "J"))  # Jello, World!

print(main_string.split(","))  # ['Hello', ' World!']

print(main_string.split(" "))  # ['Hello,', 'World!']

print(main_string[::-1])  # !dlroW ,olleH

print(main_string[0:5:2])  # Hlo

print(main_string.count("l"))  # 3

print(main_string.find("W"))  # 7

print(main_string.index("W"))  # 7

print(main_string.isalnum())  # False

print(main_string.replace("World", "Universe"))  # Hello, Universe!

print(main_string.endswith("!"))  # True


'''
Hi NS LONI
Hello LONI 'Python'
Hi NS LONI
e
llo
orl
13
hello, world!
HELLO, WORLD!
Jello, World!
['Hello', ' World!']
['Hello,', 'World!']
!dlroW ,olleH
Hlo
3
7
7
False
Hello, Universe!
True
'''