# # # num = int(input("Enter the number for table: "))

for i in range(1,11):
     print(num, "*", i, "=", num*i)

num = int(input("Enter the number for num: "))

if num <= 1:
    if num < 0:
        print("-ve num")
    else:
        print("1 is non prime") 
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if(num % i == 0):
            print == False
            break
        
    if prime == True:
        print("Prime")
    else:
        print("Not Prime")




def factorai(n):
    
    if n < 0:
        return "Enter the positive number"
    
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorai(n-1)
    
n = int(input("Entr the number for factorial: "))    
print(factorai(n))