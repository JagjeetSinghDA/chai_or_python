# number = 5 
# fact = 1 
# for num in range(1,number+1):
#     fact = num * fact
# print(fact)

number = int(input("Write the number to calculate the factorial: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(number))