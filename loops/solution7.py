

# if 1 <= number <= 10:
#     print("You have written the correct value")
# else:
#     print("Erorr")




while True:
    number = int(input("Write a number between 1 and 10: "))
    if 1 <= number <= 10:
        print("You have written the correct value")
        break
    else:
        print("Erorr: Invalid Number")