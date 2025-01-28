# 1

num = int(input("enter the number for get a table of the number:"))

for i in range(1,11):
    print(num, "*", i, "=", num*i)
    
#--------------------------------------------------------------

# 2 prime or not

num = int(input("enter the numbe rfor check whether given number is prime or not: "))
prime = True

for i in range(2,num):
    if(num % i == 0):
        prime = False
        break
if prime:
    print("Prime")
else:
    print("Not a Prime")       

#--------------------------------------------------------------
    
# factorial of a Number

def factorial(n):
    if n== 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the Number: "))    
print(factorial(n))
