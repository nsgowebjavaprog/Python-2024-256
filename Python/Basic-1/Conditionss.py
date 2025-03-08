'''
if True:
    print("Given Condition is true")
    
if 1 == 1:
    print("True")    


language = 'Python'

if language == 'Python':    # True
    print("True")
else:
    print("No Match")    
    
'''

# print("Hello--NS LONi")

user = 'admin'
login = True

if user =='admin' and login:
    print("It open a   Admin Page")
else:
    print("Not Log-In")    
    
a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))

print(a is b)    # id is diffrerent --> false

print(id(a) != id(b))   # ---> true

