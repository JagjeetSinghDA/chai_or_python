number = int(input("Write the number to check if its prime or not: "))

is_prime = True 
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

if is_prime == True:
    print(f"{number} is prime number")
else:
    print("Not a prime number")
    
print(is_prime)