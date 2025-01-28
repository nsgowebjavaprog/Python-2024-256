 # ------------> 3 + 16 + 7 => 26

# # # 1.--------------------------------------------------------------------------

num = int(input("Enter the number for table: "))
for i in range(1,11):
    print(num, "*", i, "=", num*i)

# # 2.--------------------------------------------------------------------------

num = int(input("Enter the number for check it's Prime or Not: "))

if num <= 1:
    if num < 0:
        print("Enter the number is  negative....")
    else:
        print("It's is 1 Then it's Not a prime number")    

else:
    prime = True

    for i in range(2 ,int(num ** 0.5) +1 ):
        if(num % i == 0):
            prime = False
            break
        
    if prime == True:
        print("Prime")
        
    else:
        print("Not - Prime")        

# 3.--------------------------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter the Number for Factorail Solution: "))    

print(f"Factorial of  is : {factorial(n)}")