'''
def hello_fun():
    pass
hello_fun()


# Re-Useability

def hello_func():
    # print("NS LONI")
    
    return 'Ns Loni'
    
print(hello_func())  #Need to write a print(--) Ns Loni
hello_func()
hello_func()
hello_func()    
hello_func()
'''

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Maths', 'Science', name='loni', age=21)    

'''
('Maths', 'Science')
{'name': 'loni', 'age': 21}
'''

