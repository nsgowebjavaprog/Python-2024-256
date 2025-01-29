# 1.Multiplication of two numbers  ------> 3

num = int(input("Enter the first number: "))
for i in range(1, 11):
    print(num, "*", i, " = ", num*i)


# 2. Prime or not ----> 16

num = int(input("Enter the number: "))    
if num <= 1:
    if num <0:
        print("-ve Number")
    else:
        print("Not Prime")    
else:
    prime = True
    for i in range(2, num):
        if num%i == 0:
            prime = False
            break
    if prime == True:
        print("Prime Number") 
    else:
        print("Not a Prime Number")                      
   
# 3.Factorial of Number ------> 7

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter the number for Find Factorial: "))            
print(fact(n))