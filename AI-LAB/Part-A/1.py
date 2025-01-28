'''3 '''

num = int(input("Etner the num for table: "))

for i in range(1,11):
    print(f"num * {i} = {num*i}")
    
    
'''16 '''

num = int(input("Enter the number: "))

if num <= 1:
    if num < 0:
        print("Negative Number")
    else:
        print("1 is not prime")     
else:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime")            
    else:
        print("Not Prime")

''' 7 '''

def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    
n = int(input("Enter the number: "))    
print(fac(n))