number = int(input("Write the number to calculate the factorial. "))
multiply = 1

while number > 0:
    multiply = multiply * number
    number = number - 1 
print(multiply)



for i in range(1, number + 1):
    multiply = multiply * i
print(multiply)