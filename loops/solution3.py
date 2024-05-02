number = int(input("Write the number to print its table upto 10th: "))


for i in range(1, 11):
    if i != 5:
        multiply = i * number
        print(f"{number} x {i} = {multiply}")