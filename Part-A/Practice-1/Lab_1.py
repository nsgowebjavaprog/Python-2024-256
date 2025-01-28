# # # 2 * 1 = 2 print the Table of the 'nth' Number

num = int(input("Enter the number: "))
for i in range(1,11):
    print(num, "*", i ,"=", num*i)

# # Prime or not----------------------------------------

num = int(input("Enter the Number: "))
prime = True

for i in range(2,num):
    if(num % i == 0):
        prime =  False
if prime:
    print("Prime Number")        
else:
    print("Non-Prime Number")    

# # Factorial-------------------------------------------

def factorial(n):
    if n== 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the Number: "))    
print(factorial(n))