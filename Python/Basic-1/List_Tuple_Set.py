# list []
courses = ['Math','cs','ada']
'''
print(courses)
print(len(courses))
print(type(courses))

for i in range(len(courses)):
    print(i, end=" ")
print()    

print(courses[2])

print(courses[-1])

print(courses[::1])

print(courses[::-1])

print(courses[0:2])

print(courses[1:3])

print(courses[1:])
'''
# add


courses.append('Arts')
print(courses)

courses.insert(0, 'ns-loni')
print(courses)

# ['ns-loni', 'Math', 'cs', 'ada', 'Arts']

courses.extend('loni')
print(courses)
# ['ns-loni', 'Math', 'cs', 'ada', 'Arts', 'l', 'o', 'n', 'i']

courses_1 = ['saas','ai','ml']
courses.extend(courses_1)
print(courses)
#['ns-loni', 'Math', 'cs', 'ada', 'Arts', 'l', 'o', 'n', 'i', 'saas', 'ai', 'ml']        

courses.pop()
print(courses)

courses.index('cs')
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

# OR
sorted(courses)
print(courses)

res = sorted(courses)
print(res)

print(min(courses))

print(max(courses))

# print(sum(courses))

print(slice(courses))

print(courses.index('saas'))

print('saas' in courses)

courses_1 = ['a','d','df']

courses_1.split('--')
print(courses_1)