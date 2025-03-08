# Dictionay 

# student = {'Key': "value"}

student = {'name':'Loni', 'age':21, 'sub':['Kannad', 'Computer Science']}
print(student)

print(student['name'])

print(student['age'])

# print(student['phone'])   ---> KeyError

print(student.get('phone'))  # None

student.update({'name':'NS'})
print(student)

# del student['age']
# print(student)

age = student.pop('age')
print(student)
#print(age)


print(student.values())

print(student.items())

for key, val in student.items():
    print(key, val)