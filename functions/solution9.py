
# number_limit = int(input("Write the number till where you want even numbers: "))


def get_even_num(number_limit):
    # even_numbers_list = []
    for num in range(2, number_limit + 1, 2):
        yield num 
        # print(num)
        # return num
    #     even_numbers_list.append(num)
    # return even_numbers_list

# print(get_even_num(10))
for i in get_even_num(10):
    print(i)