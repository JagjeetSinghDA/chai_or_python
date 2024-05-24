input_string = 'teabcabceterq'

for i in input_string:
    # print(i)
    if input_string.count(i) == 1:
        print(i, '*')
        break
    