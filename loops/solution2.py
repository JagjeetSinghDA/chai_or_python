nth_number = int(input("Write the number till where you want to add the even numbers: "))
sum_of_even_numbers_till_nth_number = 0

for num in range(nth_number+1):
    if num % 2 == 0:
        sum_of_even_numbers_till_nth_number = sum_of_even_numbers_till_nth_number + num

print(sum_of_even_numbers_till_nth_number)